using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;

using JYSYSTEMLIBLib;
using JYCCDLib;
using JYCONFIGBROWSERCOMPONENTLib;

namespace CCD_CS_NET
{
    public partial class Form1 : Form
    {
        private JYCONFIGBROWSERCOMPONENTLib.JYConfigBrowerInterface jyBrowser;
        private JYMCDClass jyCCD;

        private Boolean mbTemperatureCheck;

        private Boolean mbInitialized;

        // JY data definition
        public JYSYSTEMLIBLib.IJYDataObject ccdData;
        public JYSYSTEMLIBLib.IJYResultsObject ccdResult;

        // chip dimensions, etc
        int xPixels;
        int yPixels;
        int XSize;
        int ysize;
        short acqs;

        // file save format
        Boolean savespc;
        jyCCDDataType mode;
        short streaming;

        // Values to be persisted
        JYSYSTEMLIBLib.jyADCType lastADC;
        Double lastIntegrationTime;

        //=============================================
        public Form1()
        {
            InitializeComponent();
        }

        //=============================================
        private void Form1_Load(object sender, EventArgs e)
        {
            jyBrowser = new JYCONFIGBROWSERCOMPONENTLib.JYConfigBrowerInterface();
            jyBrowser.Load();
            jyCCD = new JYCCDLib.JYMCDClass();

            LoadCCDs();

            GetCCDTemperature();
        }

        //=============================================
        // Load Available CCDs into DropDown List
        //=============================================
        private void LoadCCDs()
        {
            string sDevId, sDevName = "";
            NameID CCD;
            CCD = new NameID();

            try
            {
                // Remove existing items from the control.
                DeviceCombo.Items.Clear();

                // Fill Combo Box with CCD devices
                sDevId = jyBrowser.GetFirstCCD(out sDevName);

                // Add Configuration Names to combo box
                while ((string.Compare(sDevId, "") != 0) && (string.Compare(sDevName, null) != 0))
                {
                    CCD.sDevName = sDevName;
                    CCD.sDevId = sDevId;
                    DeviceCombo.Items.Add(CCD);

                    sDevId = jyBrowser.GetNextCCD(out sDevName);
                }

                if (DeviceCombo.Items.Count >= 1)
                    DeviceCombo.SelectedIndex = 0;

                // Disable certain controls until after Connection
                CCD_InitializeBtn.Enabled = false;
                GroupBoxCCDInfo.Enabled = false;
                GroupBoxCCDSetup.Enabled = false;
                GroupBoxStreamAcq.Enabled = false;
                GroupBoxAcquire.Enabled = false;

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error Loading CCDs", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        //=============================================
        private void CCD_Connect_Click(object sender, EventArgs e)
        {
            // This set the unique id of the device the identifies the configuration to be loaded
            NameID Device;
            Device = (NameID)DeviceCombo.SelectedItem;
            jyCCD.Uniqueid = Device.sDevId;

            jyCCD._IJYDeviceReqdEvents_Event_Initialize += OnCCDEvent_Initialized;
            jyCCD.OperationStatus += OnCCDEvent_OperationStatus;
            jyCCD.Update += OnCCDEvent_Update;

            // Loads up the device with the specified configuration
            jyCCD.Load();

            // Attempts to communicate with a device on the specified communication settings (in the configuration)
            // If it fails, the OnError handler allows for the device to be emulated in software

            CCD_InitializeBtn.Enabled = false;

            try
            {
                jyCCD.OpenCommunications();

                CCD_InitializeBtn.Enabled = true;
            }
            catch (Exception ex)
            {
                if (MessageBox.Show("Hardware Not Detected. Emulate?", "Error", MessageBoxButtons.YesNo, MessageBoxIcon.Error) == DialogResult.Yes)
                {
                    jyCCD.Initialize(false, true);
                }
                else
                {
                    if (MessageBox.Show("Do You Want to Retry CCD?", "", MessageBoxButtons.YesNo, MessageBoxIcon.Error) == DialogResult.Yes)
                        CCD_Connect_Click(CCD_Connect, new System.EventArgs());
                    else
                    {
                        MessageBox.Show("No CCD Connection... Select Device and Retry", "", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        DeviceCombo.Enabled = true;
                    }
                }
            }
        }

        //=============================================
        private void CCD_InitializeBtn_Click(object sender, EventArgs e)
        {
            // disable UI
            CCD_InitializeBtn.Enabled = false;
            DeviceCombo.Enabled = false;
            SetParamsBtn.Enabled = false;
            GoBtn.Enabled = false;
            StartBtn.Enabled = false;

            // attempt to reinitialize ccd
            try
            {
                if (CCD_InitializeBtn.Text == "Reinitialize")
                    jyCCD.Initialize(true);  // True = Force Init
                else
                    jyCCD.Initialize();
            }
            catch (Exception ex)
            {
                if (MessageBox.Show("Hardware Not Detected. Emulate?", "", MessageBoxButtons.YesNo, MessageBoxIcon.Error) == DialogResult.Yes)
                    jyCCD.Initialize(false, true);
                else
                {
                    if (MessageBox.Show("Do you want to retry CCD?", "", MessageBoxButtons.YesNo, MessageBoxIcon.Error) == DialogResult.Yes)
                        CCD_InitializeBtn_Click(CCD_InitializeBtn, new System.EventArgs());
                    else
                    {
                        MessageBox.Show("No CCD Initialized... Select Device and retry", "", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        CCD_InitializeBtn.Enabled = true;
                        DeviceCombo.Enabled = true;
                    }
                }
            }
        }

        //=============================================
        public void OnCCDEvent_Initialized(int status, JYSYSTEMLIBLib.IJYEventInfo eventInfo)
        {
                // enable UI
            CCD_InitializeBtn.Text = "Reinitialize";
            CCD_InitializeBtn.Enabled = true;
            SetParamsBtn.Enabled = true;

                // get properties of the ccd
            jyCCD.GetChipSize( out xPixels, out yPixels );
            ChipX.Text = Convert.ToString( xPixels );
            ChipY.Text = Convert.ToString( yPixels );
            CCDName.Text = jyCCD.Name;
            Description.Text = jyCCD.Description;
            FWVersion.Text = jyCCD.FirmwareVersion;

            //jyCCD.TemperatureSetPoint = 283.0;      // Kelvin
            //object otemp;
            //jyUnits tempUnits;
            //jyCCD.GetDefaultUnits(jyUnitsType.jyutTemperature,out tempUnits, out otemp);
           
                // set data file save type
            savespc = true;

            InitializeInitIntegration();
            InitializeAreaInfo();
            InitializeGainSelect();
            InitializeADCSelect();

            // Enable CCD Groups
            GroupBoxCCDInfo.Enabled = true;
            GroupBoxCCDSetup.Enabled = true;
            GroupBoxStreamAcq.Enabled = true;
            GroupBoxAcquire.Enabled = true;

            // Make sure these are disabled until Set Params done
            GoBtn.Enabled = false;
            StartBtn.Enabled = false;
        }

        //=============================================
        public void OnCCDEvent_OperationStatus(int status, JYSYSTEMLIBLib.IJYEventInfo eventInfo)
        {
        }

        //=============================================
        public void OnCCDEvent_Update(int updateType, JYSYSTEMLIBLib.IJYEventInfo eventInfo)
        {
            string msg;
            Object dataArray;

            // Update type 100 indicates that this is a data update. Currently the 
            // only type of update event fired by the ccd object
            if (updateType != 100)
                return;

            StatusMessage.Text = "Acquisition Completed";

            Update_Renamed.Text = "Data Update received...";

            try
            {
                ccdResult = eventInfo.GetResult();
            }
            catch (Exception ex)
            {
                string sErr = string.Copy("Failed During Acquistion: Get Result Obj Failed");
                Update_Renamed.Text = sErr;
                msg = string.Format("{0}\r\n{1}", sErr, ex.Message);
                MessageBox.Show(msg, "Acquistion Failure", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            try
            {
                // Process the data. The following simply retrieves the dataObject 
                // from the result that carries it. This data object will be used in 
                // the event an attempt is made to save the data.
                ccdData = ccdResult.GetFirstDataObject();
                if (ccdData == null)
                {
                    string sErr = string.Copy("GetFirstDataObject() Failed: Did notGet Data Object");
                    Update_Renamed.Text = sErr;
                    MessageBox.Show(sErr, "Failed To Get Data Object", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                ccdData.GetDataAsArray(out dataArray, true, 1);
                int yyy = 0;

                int numDims = ccdData.NumberOfDimensions;
                int xdim = ccdData.GetDimension(1);
                int ydim = 1;
                if (numDims > 1)
                {
                    ydim = ccdData.GetDimension(2);
                }

                if (JYSYSTEMLIBLib.jyDataObjectDataFormat.jyDFInt32 == ccdData.DataFormat)
                {
                    // 3 ways (at least) to get the data collected.
                    Int32 firstpt, lastpt;

                    // 1st way is to pull each value out using GetValue (slowest way)
                    Array aa;
                    if (ydim > 1)
                    {
                        aa = (Array)dataArray;
                        firstpt = (Int32)aa.GetValue(0, 0);
                        lastpt = (Int32)aa.GetValue(xdim - 1, ydim - 1);
                        // 2nd way copy twodimensional array
                        Int32[,] arrptr = new Int32[xdim, ydim];
                        // copy aa array starting at first element to arrptr array starting at it's first element. copy Length elements
                        Array.Copy(aa, 0, arrptr, 0, aa.Length);
                        firstpt = arrptr[0, 0];
                        lastpt = arrptr[xdim - 1, ydim - 1];
                        // copy array as block copy (fastest way)
                        Int32[,] arrptr2 = new Int32[xdim, ydim];
                        // copy Length * size of data type bytes to array 
                        Buffer.BlockCopy(aa, 0, arrptr2, 0, aa.Length * sizeof(Int32));
                        firstpt = arrptr2[0, 0];
                        lastpt = arrptr2[xdim - 1, ydim - 1];
                    }
                    else
                    {
                        // 1st way is to pull each value out using GetValue (slowest way)
                        aa = (Array)dataArray;
                        firstpt = (Int32)aa.GetValue(0);
                        lastpt = (Int32)aa.GetValue(xdim - 1);

                        // 2nd way is to copy two-dimensional array
                        Int32[] S_arrptr = new Int32[xdim];
                        // copy aa array starting at first element to arrptr array starting at it's first element. copy Length elements
                        Array.Copy(aa, 0, S_arrptr, 0, aa.Length);
                        firstpt = S_arrptr[0];
                        lastpt = S_arrptr[xdim - 1];

                        // 3rd way is to copy array as block copy (fastest way)
                        Int32[] S_arrptr2 = new Int32[xdim];
                        // copy Length * size of data type bytes to array 
                        Buffer.BlockCopy(aa, 0, S_arrptr2, 0, aa.Length * sizeof(Int32));
                        firstpt = S_arrptr2[0];
                        lastpt = S_arrptr2[xdim - 1];
                    }


                }


 

                // Do something with data array...

            }
            catch (Exception ex)
            {
                string sErr = string.Copy("Failed During Acquistion: Get Data Obj Failed");
                Update_Renamed.Text = sErr;
                msg = string.Format("{0}\r\n{1}", sErr, ex.Message);
                MessageBox.Show(msg, "Acquistion Failure", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

            StartBtn.Enabled = true;

        }

        //=============================================
        private void InitializeInitIntegration()
        {
            double dVal;
            Object oUnits;
            string timeUnits = "";
            jyUnits units = jyUnits.jyuMilliseconds;

            try
            {
                units = jyUnits.jyuUndefined;
                jyCCD.GetDefaultUnits(jyUnitsType.jyutTime, out units, out oUnits);
                timeUnits = (String)oUnits;
            }
            catch (Exception ex)
            {
                ex.ToString();
                timeUnits = "?";
            }
            labelIntegrationTimeUnits.Text = timeUnits;

            try
            {
                dVal = jyCCD.IntegrationTime;
                if (dVal <= 0)
                    dVal = 10;
            }
            catch (Exception ex)
            {
                ex.ToString();
                dVal = 10;
            }
            IntTime.Text = dVal.ToString();
        }

        //==============================================
        // fill gain combo box with available gains
        //==============================================
        private void InitializeGainSelect()
        {
            int token;
            String sName;
            int lastGain;
            PairStringInt Gain;

            lastGain = jyCCD.Gain;

            GainList.Items.Clear();

            token = jyCCD.GetFirstGain( out sName );
            if( token == -1)
            {
                Gain = new PairStringInt();
                Gain.sVal = "NONE";
                Gain.iVal = token;
                GainList.Items.Add(Gain);
                GainList.Enabled = false;
            }
            else
            {
                while( token != -1 )
                {
                    Gain = new PairStringInt();
                    Gain.sVal = sName;
                    Gain.iVal = token;
                    GainList.Items.Add(Gain);
                    if (lastGain == token)
                        GainList.SelectedIndex = GainList.Items.Count - 1;    // Index is 0 based
                    token = jyCCD.GetNextGain( out sName );
                }
            }

            if( GainList.Items.Count == 1 )
                GainList.Enabled = false;
        }

        //==============================================
        // set basic dimensions
        //==============================================
        private void InitializeAreaInfo()
        {
            XStart.Text = "1";
            YStart.Text = "1";
            XSize = xPixels;
            ysize = yPixels;
            XBin.Text = "1";
            Spectra_CheckedChanged(Spectra, new System.EventArgs());
            XEnd.Text = Convert.ToString(xPixels);
            YEnd.Text = Convert.ToString(yPixels);
        }

        //==============================================
        // build ADC list in combo box
        //==============================================
        private void InitializeADCSelect()
        {
            int token, lastToken;
            String sName;
            int currentADC;
            ADCStringType ADC;

            // Enumerate all the available ADC's and allow user selection via the combo box
            ADCSelect.Items.Clear();

            // Get the currently selected ADC so we can select it programmatically when we come
            // across it in the enumeration
            currentADC = jyCCD.CurrentADC;
            token = jyCCD.GetFirstADC(out sName);
            lastToken = 0;
            if (token == -1)
            {
                ADC = new ADCStringType();
                ADC.sVal = "NONE";
                ADC.adcType = (jyADCType)token;
                ADCSelect.Items.Add(ADC);
                ADCSelect.Enabled = false;
            }
            else
            {
                while (token != -1)
                {
                    ADC = new ADCStringType();
                    ADC.sVal = sName;
                    ADC.adcType = (jyADCType)token;
                    ADCSelect.Items.Add(ADC);
                    if (token == currentADC)
                        ADCSelect.SelectedIndex = ADCSelect.Items.Count - 1;    // Index is 0 based
                    else
                        lastToken = ADCSelect.Items.Count - 1; 
                    token = jyCCD.GetNextADC(out sName);
                }
                // if token doesn't match any of the adc then set to first ADC
                if (ADCSelect.SelectedIndex == -1)
                {
                    ADCSelect.SelectedIndex = lastToken;
                }
            }

            // If there is only 1 adc available, disable the option of selection
            if (ADCSelect.Items.Count == 1)
                ADCSelect.Enabled = false;
        }

        //=============================================
        private void GetCCDTemperature()
        {
            double dVal;

            try
            {
                dVal = jyCCD.CurrentTemperature;
                labelTempVal.Text = dVal.ToString();
            }
            catch (Exception ex)
            {
                ex.ToString();
                labelTempVal.Text = "";
            }
        }

        //=============================================
        private void timerTemperature_Tick(object sender, EventArgs e)
        {
            if (mbTemperatureCheck == true)
                GetCCDTemperature();
        }

        //=============================================
        private void checkTemp_CheckedChanged(object sender, EventArgs e)
        {
            mbTemperatureCheck = checkTemp.Checked;
            timerTemperature.Enabled = mbTemperatureCheck;
            if (mbTemperatureCheck == false)
                labelTempVal.Text = "";
        }

        //==============================================
        // set gain from combo box
        //==============================================
        private void GainList_SelectedIndexChanged(object sender, EventArgs e)
        {
            PairStringInt Gain;
            Gain = (PairStringInt)GainList.SelectedItem;
            jyCCD.Gain = Gain.iVal;
        }

        //==============================================
        // set for spectral mode acquisition
        //==============================================
        private void Spectra_CheckedChanged(object sender, EventArgs e)
        {
            if (((RadioButton)sender).Checked)
            {
                mode = jyCCDDataType.JYMCD_ACQ_FORMAT_SCAN;

                // For spectra, force yBin = ySize
                YBin.Text = string.Format("{0:D}", ysize);
            }
        }

        //=================================
        // set for image mode
        //=================================
        private void Image_CheckedChanged(object sender, EventArgs e)
        {
            if (((RadioButton)sender).Checked)
            {
                mode = jyCCDDataType.JYMCD_ACQ_FORMAT_IMAGE;

                // For image, force yBin = 1
                YBin.Text = "1";
            }
        }

        //==============================================
        // set scan parameters
        //==============================================
        private void SetParamsBtn_Click(object sender, EventArgs e)
        {
            int X;
            
                // Set the gain
            GainList_SelectedIndexChanged( GainList, new System.EventArgs() );

                // select the ADC
            ADCStringType ADC;
            ADC = (ADCStringType)ADCSelect.SelectedItem;
            try
            {
                jyCCD.SelectADC(ADC.adcType);
                lastADC = ADC.adcType;
            }
            catch( Exception ex )
            {
                ex.ToString();
            }

                // set other properties
            if (String.IsNullOrEmpty(IntTime.Text))
            {
                jyCCD.IntegrationTime = 0.0;
                IntTime.Text = "0.0";
            }
            else
            {
                jyCCD.IntegrationTime = Convert.ToDouble(IntTime.Text);
            }
            jyCCD.DefineAcquisitionFormat( mode, 1 );
            jyCCD.DefineArea( 1, Convert.ToInt32(XStart.Text), Convert.ToInt32(YStart.Text), (int)(Convert.ToDouble(XEnd.Text) - Convert.ToDouble(XStart.Text) + 1), (int)(Convert.ToDouble(YEnd.Text) - Convert.ToDouble(YStart.Text) + 1), Convert.ToInt32(XBin.Text), Convert.ToInt32(YBin.Text) );
            X = jyCCD.DataSize;

            if( !jyCCD.ReadyForAcquisition )
            {
                MessageBox.Show( "CCD Not Ready for Acquisition. Check Debug Output", "Error", MessageBoxButtons.YesNo, MessageBoxIcon.Error );
                return;
            }

                // enable UI
            GoBtn.Enabled = true;
            StartBtn.Enabled = true;
        }

        //==============================================
        // start acquisition
        //==============================================
        private void StartBtn_Click(object sender, EventArgs e)
        {
            StartBtn.Enabled = false;

            StatusMessage.Text = "Collecting...";
            Update_Renamed.Text = "...";
            Application.DoEvents();

            // The DoAcquisition starts an acqusition on a background thread.
            // An "Update" event will be fired when the data is available
            // The option on the DoAcquisition
            Boolean shutterOpen;
            shutterOpen = true;
            jyCCD.DoAcquisition(shutterOpen);
        }

        //=====================================================
        // save data from ccd as either spc or tab delimited
        //=====================================================
        private void SaveBtn_Click(object sender, EventArgs e)
        {
            String saveFileName;

            saveFileName = FileName.Text;
            try
            {
                if (savespc)
                {
                    ccdData.FileType = JYSYSTEMLIBLib.jySupportedFileType.jySPC;
                    ccdData.Save(saveFileName);
                }
                else
                {
                    ccdData.FileType = JYSYSTEMLIBLib.jySupportedFileType.jyTabDelimitted;
                    ccdData.Save(saveFileName);
                }
            }
            catch
            {
                MessageBox.Show("Couldn't open data file, make sure folder exists", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
        }

        //==============================================
        // select simple loop streaming acquisition
        //==============================================
        private void Option1_CheckedChanged(object sender, EventArgs e)
        {
            if (((RadioButton)sender).Checked)
                streaming = 1;
        }

        //==============================================
        // select simple loop streaming acquisition, save to memory
        //==============================================
        private void Option2_CheckedChanged(object sender, EventArgs e)
        {
            if (((RadioButton)sender).Checked)
                streaming = 2;
        }

        //==============================================
        // select simple loop streaming acquisition, save to files
        //==============================================
        private void Option3_CheckedChanged(object sender, EventArgs e)
        {
            if (((RadioButton)sender).Checked)
                streaming = 3;
        }

        //=================================
        // begin streaming mode
        //=================================
        private void GoBtn_Click(object sender, EventArgs e)
        {
            int counter, total_count;
            String fname;
            Boolean busy;

            counter = 1;
            total_count = Convert.ToInt16( Count.Text );

            JYSYSTEMLIBLib.IJYDataObject[] dataarray;
            dataarray = new JYSYSTEMLIBLib.IJYDataObject[total_count];

            do
            {
                // display counter
                label_IterationValue.Text = counter.ToString();
                Application.DoEvents();

                // Start data Acquisition
                jyCCD.StartAcquisition( true );
                // wait for data to come in (busy = False)
                do
                    busy = jyCCD.AcquisitionBusy();
                while( busy == true );

                // Get result of data acquisition
                ccdResult = jyCCD.GetResult();
                // pull off as data object
                ccdData = ccdResult.GetFirstDataObject();

                if (streaming == 1)
                {
                    // pull of number of dimensions
                    int numOfDim = ccdData.NumberOfDimensions;
                    // int numXDim = ccdData.Dimensions;
                    int numXDim = ccdData.GetDimension(1);  // x dimension
                    int numYDim=1;
                    // get y dimension if dimensions > 1
                    if (numOfDim > 1)
                        numYDim = ccdData.GetDimension(2);  // y dimension
                    object test;
                    // pull off data into object (safearray)
                    ccdData.GetDataAsArray(out test);
                   
                    // do something with the data
                }
                if (streaming == 2)
                {
                    // make a copy of data and store in array of data objects
                    dataarray[counter - 1] = ccdData.MakeCopy();
                }

                if( streaming == 3 )
                {
                    fname = Path.GetFullPath(FileName.Text) +
                            Path.GetFileNameWithoutExtension(FileName.Text) +
                            Convert.ToString(counter) +
                            Path.GetExtension(FileName.Text);
                    try
                    {
                        // Save each Collection into a unique file
                        ccdData.Save(fname);
                    }
                    catch
                    {
                        MessageBox.Show("Couldn't open data file, make sure folder exists", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        return;
                    }
                }

                counter = counter + 1;
            }            
            while( counter <= total_count );

            // if streaming to memory, the loop through array and write each image to file
            if (streaming == 2)
            {
                try
                {
                    for (counter = 0; counter < total_count; counter++)
                    {
                        fname = Path.GetFullPath(FileName.Text) +
                                Path.GetFileNameWithoutExtension(FileName.Text) +
                                Convert.ToString(counter+1) +
                                Path.GetExtension(FileName.Text);
                        // Save each Collection into a unique file
                        dataarray[counter].Save(fname);
                    }
                }
                catch
                {
                    MessageBox.Show("Couldn't open data file, make sure folder exists", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }
            }
        }


        //=============================================
        public class PairStringLong
        {
            public String sVal;
            public long lVal;
            public override String ToString()
            {
                return sVal.ToString();
            }
        }

        //=============================================
        public class ADCStringType
        {
            public String sVal;
            public JYSYSTEMLIBLib.jyADCType adcType;
            public override String ToString()
            {
                return sVal.ToString();
            }
        }

        //=============================================
        public class PairStringInt
        {
            public String sVal;
            public int iVal;
            public override String ToString()
            {
                return sVal.ToString();
            }
        }

        //=============================================
        public class NameID
        {
            public String sDevName;
            public String sDevId;
            public override String ToString()
            {
                return sDevName.ToString();
            }
        }

        private void multiChannelDetectorToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // This set the unique id of the device the identifies the configuration to be loaded
            NameID CCD;
            try
            {
                CCD = (NameID)DeviceCombo.SelectedItem;
                jyCCD.Uniqueid = CCD.sDevId;

                // Loads up the device with the specified configuration
                jyCCD.Load();
                jyCCD.Configure();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error Configuring Selected MCD", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }
 
    }
}
