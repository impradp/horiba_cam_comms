namespace CCD_CS_NET
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.mnuConfigure = new System.Windows.Forms.ToolStripMenuItem();
            this.multiChannelDetectorToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.CCD_InitializeBtn = new System.Windows.Forms.Button();
            this.CCD_Connect = new System.Windows.Forms.Button();
            this.DeviceCombo = new System.Windows.Forms.ComboBox();
            this.GroupBoxCCDInfo = new System.Windows.Forms.GroupBox();
            this.Description = new System.Windows.Forms.Label();
            this.label18 = new System.Windows.Forms.Label();
            this.FWVersion = new System.Windows.Forms.Label();
            this.label16 = new System.Windows.Forms.Label();
            this.ChipY = new System.Windows.Forms.Label();
            this.label17 = new System.Windows.Forms.Label();
            this.ChipX = new System.Windows.Forms.Label();
            this.label15 = new System.Windows.Forms.Label();
            this.CCDName = new System.Windows.Forms.Label();
            this.label14 = new System.Windows.Forms.Label();
            this.labelTempVal = new System.Windows.Forms.Label();
            this.checkTemp = new System.Windows.Forms.CheckBox();
            this.timerTemperature = new System.Windows.Forms.Timer(this.components);
            this.GroupBoxCCDSetup = new System.Windows.Forms.GroupBox();
            this.SetParamsBtn = new System.Windows.Forms.Button();
            this.YBin = new System.Windows.Forms.TextBox();
            this.label9 = new System.Windows.Forms.Label();
            this.XBin = new System.Windows.Forms.TextBox();
            this.label8 = new System.Windows.Forms.Label();
            this.YEnd = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.XEnd = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.YStart = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.XStart = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.Image = new System.Windows.Forms.RadioButton();
            this.Spectra = new System.Windows.Forms.RadioButton();
            this.ADCSelect = new System.Windows.Forms.ComboBox();
            this.label3 = new System.Windows.Forms.Label();
            this.GainList = new System.Windows.Forms.ComboBox();
            this.label2 = new System.Windows.Forms.Label();
            this.labelIntegrationTimeUnits = new System.Windows.Forms.Label();
            this.IntTime = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.GroupBoxStreamAcq = new System.Windows.Forms.GroupBox();
            this.label_IterationValue = new System.Windows.Forms.Label();
            this.GoBtn = new System.Windows.Forms.Button();
            this.FileName = new System.Windows.Forms.TextBox();
            this.label13 = new System.Windows.Forms.Label();
            this.label12 = new System.Windows.Forms.Label();
            this.Count = new System.Windows.Forms.TextBox();
            this.label10 = new System.Windows.Forms.Label();
            this.Option3 = new System.Windows.Forms.RadioButton();
            this.Option2 = new System.Windows.Forms.RadioButton();
            this.Option1 = new System.Windows.Forms.RadioButton();
            this.GroupBoxAcquire = new System.Windows.Forms.GroupBox();
            this.SaveBtn = new System.Windows.Forms.Button();
            this.Update_Renamed = new System.Windows.Forms.Label();
            this.label20 = new System.Windows.Forms.Label();
            this.StatusMessage = new System.Windows.Forms.Label();
            this.label19 = new System.Windows.Forms.Label();
            this.StartBtn = new System.Windows.Forms.Button();
            this.menuStrip1.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.GroupBoxCCDInfo.SuspendLayout();
            this.GroupBoxCCDSetup.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.GroupBoxStreamAcq.SuspendLayout();
            this.GroupBoxAcquire.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuConfigure});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Padding = new System.Windows.Forms.Padding(5, 2, 0, 2);
            this.menuStrip1.Size = new System.Drawing.Size(561, 28);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // mnuConfigure
            // 
            this.mnuConfigure.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.multiChannelDetectorToolStripMenuItem});
            this.mnuConfigure.Name = "mnuConfigure";
            this.mnuConfigure.Size = new System.Drawing.Size(86, 24);
            this.mnuConfigure.Text = "Configure";
            // 
            // multiChannelDetectorToolStripMenuItem
            // 
            this.multiChannelDetectorToolStripMenuItem.CheckOnClick = true;
            this.multiChannelDetectorToolStripMenuItem.Name = "multiChannelDetectorToolStripMenuItem";
            this.multiChannelDetectorToolStripMenuItem.Size = new System.Drawing.Size(233, 24);
            this.multiChannelDetectorToolStripMenuItem.Text = "Multi-Channel Detector";
            this.multiChannelDetectorToolStripMenuItem.Click += new System.EventHandler(this.multiChannelDetectorToolStripMenuItem_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.CCD_InitializeBtn);
            this.groupBox1.Controls.Add(this.CCD_Connect);
            this.groupBox1.Controls.Add(this.DeviceCombo);
            this.groupBox1.Location = new System.Drawing.Point(11, 39);
            this.groupBox1.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Padding = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.groupBox1.Size = new System.Drawing.Size(331, 81);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Device Selection";
            // 
            // CCD_InitializeBtn
            // 
            this.CCD_InitializeBtn.Location = new System.Drawing.Point(237, 30);
            this.CCD_InitializeBtn.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.CCD_InitializeBtn.Name = "CCD_InitializeBtn";
            this.CCD_InitializeBtn.Size = new System.Drawing.Size(85, 31);
            this.CCD_InitializeBtn.TabIndex = 2;
            this.CCD_InitializeBtn.Text = "Initialize";
            this.CCD_InitializeBtn.UseVisualStyleBackColor = true;
            this.CCD_InitializeBtn.Click += new System.EventHandler(this.CCD_InitializeBtn_Click);
            // 
            // CCD_Connect
            // 
            this.CCD_Connect.Location = new System.Drawing.Point(144, 30);
            this.CCD_Connect.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.CCD_Connect.Name = "CCD_Connect";
            this.CCD_Connect.Size = new System.Drawing.Size(81, 31);
            this.CCD_Connect.TabIndex = 1;
            this.CCD_Connect.Text = "Connect";
            this.CCD_Connect.UseVisualStyleBackColor = true;
            this.CCD_Connect.Click += new System.EventHandler(this.CCD_Connect_Click);
            // 
            // DeviceCombo
            // 
            this.DeviceCombo.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.DeviceCombo.FormattingEnabled = true;
            this.DeviceCombo.Location = new System.Drawing.Point(13, 34);
            this.DeviceCombo.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.DeviceCombo.Name = "DeviceCombo";
            this.DeviceCombo.Size = new System.Drawing.Size(119, 24);
            this.DeviceCombo.TabIndex = 0;
            // 
            // GroupBoxCCDInfo
            // 
            this.GroupBoxCCDInfo.Controls.Add(this.Description);
            this.GroupBoxCCDInfo.Controls.Add(this.label18);
            this.GroupBoxCCDInfo.Controls.Add(this.FWVersion);
            this.GroupBoxCCDInfo.Controls.Add(this.label16);
            this.GroupBoxCCDInfo.Controls.Add(this.ChipY);
            this.GroupBoxCCDInfo.Controls.Add(this.label17);
            this.GroupBoxCCDInfo.Controls.Add(this.ChipX);
            this.GroupBoxCCDInfo.Controls.Add(this.label15);
            this.GroupBoxCCDInfo.Controls.Add(this.CCDName);
            this.GroupBoxCCDInfo.Controls.Add(this.label14);
            this.GroupBoxCCDInfo.Controls.Add(this.labelTempVal);
            this.GroupBoxCCDInfo.Controls.Add(this.checkTemp);
            this.GroupBoxCCDInfo.Location = new System.Drawing.Point(349, 50);
            this.GroupBoxCCDInfo.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.GroupBoxCCDInfo.Name = "GroupBoxCCDInfo";
            this.GroupBoxCCDInfo.Padding = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.GroupBoxCCDInfo.Size = new System.Drawing.Size(201, 311);
            this.GroupBoxCCDInfo.TabIndex = 3;
            this.GroupBoxCCDInfo.TabStop = false;
            this.GroupBoxCCDInfo.Text = "Info";
            // 
            // Description
            // 
            this.Description.AutoSize = true;
            this.Description.Location = new System.Drawing.Point(11, 220);
            this.Description.Name = "Description";
            this.Description.Size = new System.Drawing.Size(31, 17);
            this.Description.TabIndex = 11;
            this.Description.Text = "N/A";
            // 
            // label18
            // 
            this.label18.AutoSize = true;
            this.label18.Location = new System.Drawing.Point(11, 199);
            this.label18.Name = "label18";
            this.label18.Size = new System.Drawing.Size(83, 17);
            this.label18.TabIndex = 10;
            this.label18.Text = "Description:";
            // 
            // FWVersion
            // 
            this.FWVersion.AutoSize = true;
            this.FWVersion.Location = new System.Drawing.Point(11, 170);
            this.FWVersion.Name = "FWVersion";
            this.FWVersion.Size = new System.Drawing.Size(31, 17);
            this.FWVersion.TabIndex = 9;
            this.FWVersion.Text = "N/A";
            // 
            // label16
            // 
            this.label16.AutoSize = true;
            this.label16.Location = new System.Drawing.Point(11, 150);
            this.label16.Name = "label16";
            this.label16.Size = new System.Drawing.Size(121, 17);
            this.label16.TabIndex = 8;
            this.label16.Text = "Firmware Version:";
            // 
            // ChipY
            // 
            this.ChipY.AutoSize = true;
            this.ChipY.Location = new System.Drawing.Point(60, 121);
            this.ChipY.Name = "ChipY";
            this.ChipY.Size = new System.Drawing.Size(31, 17);
            this.ChipY.TabIndex = 7;
            this.ChipY.Text = "N/A";
            // 
            // label17
            // 
            this.label17.AutoSize = true;
            this.label17.Location = new System.Drawing.Point(11, 121);
            this.label17.Name = "label17";
            this.label17.Size = new System.Drawing.Size(53, 17);
            this.label17.TabIndex = 6;
            this.label17.Text = "Chip Y:";
            // 
            // ChipX
            // 
            this.ChipX.AutoSize = true;
            this.ChipX.Location = new System.Drawing.Point(60, 90);
            this.ChipX.Name = "ChipX";
            this.ChipX.Size = new System.Drawing.Size(31, 17);
            this.ChipX.TabIndex = 5;
            this.ChipX.Text = "N/A";
            // 
            // label15
            // 
            this.label15.AutoSize = true;
            this.label15.Location = new System.Drawing.Point(11, 90);
            this.label15.Name = "label15";
            this.label15.Size = new System.Drawing.Size(53, 17);
            this.label15.TabIndex = 4;
            this.label15.Text = "Chip X:";
            // 
            // CCDName
            // 
            this.CCDName.AutoSize = true;
            this.CCDName.Location = new System.Drawing.Point(60, 60);
            this.CCDName.Name = "CCDName";
            this.CCDName.Size = new System.Drawing.Size(31, 17);
            this.CCDName.TabIndex = 3;
            this.CCDName.Text = "N/A";
            // 
            // label14
            // 
            this.label14.AutoSize = true;
            this.label14.Location = new System.Drawing.Point(11, 60);
            this.label14.Name = "label14";
            this.label14.Size = new System.Drawing.Size(49, 17);
            this.label14.TabIndex = 2;
            this.label14.Text = "Name:";
            // 
            // labelTempVal
            // 
            this.labelTempVal.AutoSize = true;
            this.labelTempVal.Location = new System.Drawing.Point(79, 32);
            this.labelTempVal.Name = "labelTempVal";
            this.labelTempVal.Size = new System.Drawing.Size(101, 17);
            this.labelTempVal.TabIndex = 1;
            this.labelTempVal.Text = "<temperature>";
            // 
            // checkTemp
            // 
            this.checkTemp.AutoSize = true;
            this.checkTemp.Location = new System.Drawing.Point(11, 30);
            this.checkTemp.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.checkTemp.Name = "checkTemp";
            this.checkTemp.Size = new System.Drawing.Size(66, 21);
            this.checkTemp.TabIndex = 0;
            this.checkTemp.Text = "Temp";
            this.checkTemp.UseVisualStyleBackColor = true;
            this.checkTemp.CheckedChanged += new System.EventHandler(this.checkTemp_CheckedChanged);
            // 
            // timerTemperature
            // 
            this.timerTemperature.Interval = 1000;
            this.timerTemperature.Tick += new System.EventHandler(this.timerTemperature_Tick);
            // 
            // GroupBoxCCDSetup
            // 
            this.GroupBoxCCDSetup.Controls.Add(this.SetParamsBtn);
            this.GroupBoxCCDSetup.Controls.Add(this.YBin);
            this.GroupBoxCCDSetup.Controls.Add(this.label9);
            this.GroupBoxCCDSetup.Controls.Add(this.XBin);
            this.GroupBoxCCDSetup.Controls.Add(this.label8);
            this.GroupBoxCCDSetup.Controls.Add(this.YEnd);
            this.GroupBoxCCDSetup.Controls.Add(this.label7);
            this.GroupBoxCCDSetup.Controls.Add(this.XEnd);
            this.GroupBoxCCDSetup.Controls.Add(this.label6);
            this.GroupBoxCCDSetup.Controls.Add(this.YStart);
            this.GroupBoxCCDSetup.Controls.Add(this.label5);
            this.GroupBoxCCDSetup.Controls.Add(this.XStart);
            this.GroupBoxCCDSetup.Controls.Add(this.label4);
            this.GroupBoxCCDSetup.Controls.Add(this.groupBox4);
            this.GroupBoxCCDSetup.Controls.Add(this.ADCSelect);
            this.GroupBoxCCDSetup.Controls.Add(this.label3);
            this.GroupBoxCCDSetup.Controls.Add(this.GainList);
            this.GroupBoxCCDSetup.Controls.Add(this.label2);
            this.GroupBoxCCDSetup.Controls.Add(this.labelIntegrationTimeUnits);
            this.GroupBoxCCDSetup.Controls.Add(this.IntTime);
            this.GroupBoxCCDSetup.Controls.Add(this.label1);
            this.GroupBoxCCDSetup.Location = new System.Drawing.Point(11, 140);
            this.GroupBoxCCDSetup.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.GroupBoxCCDSetup.Name = "GroupBoxCCDSetup";
            this.GroupBoxCCDSetup.Padding = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.GroupBoxCCDSetup.Size = new System.Drawing.Size(331, 241);
            this.GroupBoxCCDSetup.TabIndex = 4;
            this.GroupBoxCCDSetup.TabStop = false;
            this.GroupBoxCCDSetup.Text = "Setup";
            // 
            // SetParamsBtn
            // 
            this.SetParamsBtn.Location = new System.Drawing.Point(11, 199);
            this.SetParamsBtn.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.SetParamsBtn.Name = "SetParamsBtn";
            this.SetParamsBtn.Size = new System.Drawing.Size(111, 31);
            this.SetParamsBtn.TabIndex = 20;
            this.SetParamsBtn.Text = "Set Params";
            this.SetParamsBtn.UseVisualStyleBackColor = true;
            this.SetParamsBtn.Click += new System.EventHandler(this.SetParamsBtn_Click);
            // 
            // YBin
            // 
            this.YBin.Location = new System.Drawing.Point(280, 199);
            this.YBin.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.YBin.Name = "YBin";
            this.YBin.Size = new System.Drawing.Size(41, 22);
            this.YBin.TabIndex = 19;
            this.YBin.Text = "1";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(229, 204);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(41, 17);
            this.label9.TabIndex = 18;
            this.label9.Text = "Y Bin";
            // 
            // XBin
            // 
            this.XBin.Location = new System.Drawing.Point(280, 170);
            this.XBin.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.XBin.Name = "XBin";
            this.XBin.Size = new System.Drawing.Size(41, 22);
            this.XBin.TabIndex = 17;
            this.XBin.Text = "1";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(229, 174);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(41, 17);
            this.label8.TabIndex = 16;
            this.label8.Text = "X Bin";
            // 
            // YEnd
            // 
            this.YEnd.Location = new System.Drawing.Point(280, 142);
            this.YEnd.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.YEnd.Name = "YEnd";
            this.YEnd.Size = new System.Drawing.Size(41, 22);
            this.YEnd.TabIndex = 15;
            this.YEnd.Text = "256";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(229, 144);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(17, 17);
            this.label7.TabIndex = 14;
            this.label7.Text = "Y";
            // 
            // XEnd
            // 
            this.XEnd.Location = new System.Drawing.Point(280, 111);
            this.XEnd.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.XEnd.Name = "XEnd";
            this.XEnd.Size = new System.Drawing.Size(41, 22);
            this.XEnd.TabIndex = 13;
            this.XEnd.Text = "1024";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(229, 114);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(17, 17);
            this.label6.TabIndex = 12;
            this.label6.Text = "X";
            // 
            // YStart
            // 
            this.YStart.Location = new System.Drawing.Point(280, 81);
            this.YStart.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.YStart.Name = "YStart";
            this.YStart.Size = new System.Drawing.Size(41, 22);
            this.YStart.TabIndex = 11;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(229, 84);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(51, 17);
            this.label5.TabIndex = 10;
            this.label5.Text = "Y Start";
            // 
            // XStart
            // 
            this.XStart.Location = new System.Drawing.Point(280, 50);
            this.XStart.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.XStart.Name = "XStart";
            this.XStart.Size = new System.Drawing.Size(41, 22);
            this.XStart.TabIndex = 9;
            this.XStart.Text = "1";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(229, 54);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(51, 17);
            this.label4.TabIndex = 8;
            this.label4.Text = "X Start";
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.Image);
            this.groupBox4.Controls.Add(this.Spectra);
            this.groupBox4.Location = new System.Drawing.Point(11, 121);
            this.groupBox4.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Padding = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.groupBox4.Size = new System.Drawing.Size(181, 66);
            this.groupBox4.TabIndex = 7;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "Acq Format";
            // 
            // Image
            // 
            this.Image.AutoSize = true;
            this.Image.Checked = true;
            this.Image.Location = new System.Drawing.Point(99, 28);
            this.Image.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.Image.Name = "Image";
            this.Image.Size = new System.Drawing.Size(67, 21);
            this.Image.TabIndex = 1;
            this.Image.TabStop = true;
            this.Image.Text = "Image";
            this.Image.UseVisualStyleBackColor = true;
            this.Image.CheckedChanged += new System.EventHandler(this.Image_CheckedChanged);
            // 
            // Spectra
            // 
            this.Spectra.AutoSize = true;
            this.Spectra.Location = new System.Drawing.Point(11, 28);
            this.Spectra.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.Spectra.Name = "Spectra";
            this.Spectra.Size = new System.Drawing.Size(78, 21);
            this.Spectra.TabIndex = 0;
            this.Spectra.Text = "Spectra";
            this.Spectra.UseVisualStyleBackColor = true;
            this.Spectra.CheckedChanged += new System.EventHandler(this.Spectra_CheckedChanged);
            // 
            // ADCSelect
            // 
            this.ADCSelect.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.ADCSelect.FormattingEnabled = true;
            this.ADCSelect.Location = new System.Drawing.Point(60, 80);
            this.ADCSelect.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.ADCSelect.Name = "ADCSelect";
            this.ADCSelect.Size = new System.Drawing.Size(131, 24);
            this.ADCSelect.TabIndex = 6;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(11, 85);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(36, 17);
            this.label3.TabIndex = 5;
            this.label3.Text = "ADC";
            // 
            // GainList
            // 
            this.GainList.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.GainList.FormattingEnabled = true;
            this.GainList.Location = new System.Drawing.Point(60, 50);
            this.GainList.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.GainList.Name = "GainList";
            this.GainList.Size = new System.Drawing.Size(161, 24);
            this.GainList.TabIndex = 4;
            this.GainList.SelectedIndexChanged += new System.EventHandler(this.GainList_SelectedIndexChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(11, 54);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(38, 17);
            this.label2.TabIndex = 3;
            this.label2.Text = "Gain";
            // 
            // labelIntegrationTimeUnits
            // 
            this.labelIntegrationTimeUnits.AutoSize = true;
            this.labelIntegrationTimeUnits.Location = new System.Drawing.Point(197, 23);
            this.labelIntegrationTimeUnits.Name = "labelIntegrationTimeUnits";
            this.labelIntegrationTimeUnits.Size = new System.Drawing.Size(54, 17);
            this.labelIntegrationTimeUnits.TabIndex = 2;
            this.labelIntegrationTimeUnits.Text = "<units>";
            // 
            // IntTime
            // 
            this.IntTime.Location = new System.Drawing.Point(120, 20);
            this.IntTime.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.IntTime.Name = "IntTime";
            this.IntTime.Size = new System.Drawing.Size(71, 22);
            this.IntTime.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(11, 23);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(110, 17);
            this.label1.TabIndex = 0;
            this.label1.Text = "Integration Time";
            // 
            // GroupBoxStreamAcq
            // 
            this.GroupBoxStreamAcq.Controls.Add(this.label_IterationValue);
            this.GroupBoxStreamAcq.Controls.Add(this.GoBtn);
            this.GroupBoxStreamAcq.Controls.Add(this.FileName);
            this.GroupBoxStreamAcq.Controls.Add(this.label13);
            this.GroupBoxStreamAcq.Controls.Add(this.label12);
            this.GroupBoxStreamAcq.Controls.Add(this.Count);
            this.GroupBoxStreamAcq.Controls.Add(this.label10);
            this.GroupBoxStreamAcq.Controls.Add(this.Option3);
            this.GroupBoxStreamAcq.Controls.Add(this.Option2);
            this.GroupBoxStreamAcq.Controls.Add(this.Option1);
            this.GroupBoxStreamAcq.Location = new System.Drawing.Point(11, 390);
            this.GroupBoxStreamAcq.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.GroupBoxStreamAcq.Name = "GroupBoxStreamAcq";
            this.GroupBoxStreamAcq.Padding = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.GroupBoxStreamAcq.Size = new System.Drawing.Size(331, 201);
            this.GroupBoxStreamAcq.TabIndex = 5;
            this.GroupBoxStreamAcq.TabStop = false;
            this.GroupBoxStreamAcq.Text = "Stream Acquisition";
            // 
            // label_IterationValue
            // 
            this.label_IterationValue.AutoSize = true;
            this.label_IterationValue.Location = new System.Drawing.Point(272, 90);
            this.label_IterationValue.Name = "label_IterationValue";
            this.label_IterationValue.Size = new System.Drawing.Size(31, 17);
            this.label_IterationValue.TabIndex = 6;
            this.label_IterationValue.Text = "N/A";
            // 
            // GoBtn
            // 
            this.GoBtn.Location = new System.Drawing.Point(251, 20);
            this.GoBtn.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.GoBtn.Name = "GoBtn";
            this.GoBtn.Size = new System.Drawing.Size(71, 31);
            this.GoBtn.TabIndex = 9;
            this.GoBtn.Text = "Go";
            this.GoBtn.UseVisualStyleBackColor = true;
            this.GoBtn.Click += new System.EventHandler(this.GoBtn_Click);
            // 
            // FileName
            // 
            this.FileName.Location = new System.Drawing.Point(77, 121);
            this.FileName.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.FileName.Name = "FileName";
            this.FileName.Size = new System.Drawing.Size(124, 22);
            this.FileName.TabIndex = 8;
            this.FileName.Text = "c:\\temp\\mydata.txt";
            // 
            // label13
            // 
            this.label13.AutoSize = true;
            this.label13.Location = new System.Drawing.Point(11, 123);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(67, 17);
            this.label13.TabIndex = 7;
            this.label13.Text = "File Path:";
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Location = new System.Drawing.Point(211, 90);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(63, 17);
            this.label12.TabIndex = 6;
            this.label12.Text = "Iteration:";
            // 
            // Count
            // 
            this.Count.Location = new System.Drawing.Point(69, 90);
            this.Count.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.Count.Name = "Count";
            this.Count.Size = new System.Drawing.Size(51, 22);
            this.Count.TabIndex = 4;
            this.Count.Text = "1";
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(11, 90);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(49, 17);
            this.label10.TabIndex = 3;
            this.label10.Text = "Count:";
            // 
            // Option3
            // 
            this.Option3.AutoSize = true;
            this.Option3.Location = new System.Drawing.Point(11, 60);
            this.Option3.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.Option3.Name = "Option3";
            this.Option3.Size = new System.Drawing.Size(110, 21);
            this.Option3.TabIndex = 2;
            this.Option3.Text = "Save to Files";
            this.Option3.UseVisualStyleBackColor = true;
            this.Option3.CheckedChanged += new System.EventHandler(this.Option3_CheckedChanged);
            // 
            // Option2
            // 
            this.Option2.AutoSize = true;
            this.Option2.Location = new System.Drawing.Point(11, 39);
            this.Option2.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.Option2.Name = "Option2";
            this.Option2.Size = new System.Drawing.Size(131, 21);
            this.Option2.TabIndex = 1;
            this.Option2.Text = "Save to Memory";
            this.Option2.UseVisualStyleBackColor = true;
            this.Option2.CheckedChanged += new System.EventHandler(this.Option2_CheckedChanged);
            // 
            // Option1
            // 
            this.Option1.AutoSize = true;
            this.Option1.Checked = true;
            this.Option1.Location = new System.Drawing.Point(11, 20);
            this.Option1.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.Option1.Name = "Option1";
            this.Option1.Size = new System.Drawing.Size(107, 21);
            this.Option1.TabIndex = 0;
            this.Option1.TabStop = true;
            this.Option1.Text = "Simple Loop";
            this.Option1.UseVisualStyleBackColor = true;
            this.Option1.CheckedChanged += new System.EventHandler(this.Option1_CheckedChanged);
            // 
            // GroupBoxAcquire
            // 
            this.GroupBoxAcquire.Controls.Add(this.SaveBtn);
            this.GroupBoxAcquire.Controls.Add(this.Update_Renamed);
            this.GroupBoxAcquire.Controls.Add(this.label20);
            this.GroupBoxAcquire.Controls.Add(this.StatusMessage);
            this.GroupBoxAcquire.Controls.Add(this.label19);
            this.GroupBoxAcquire.Controls.Add(this.StartBtn);
            this.GroupBoxAcquire.Location = new System.Drawing.Point(349, 370);
            this.GroupBoxAcquire.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.GroupBoxAcquire.Name = "GroupBoxAcquire";
            this.GroupBoxAcquire.Padding = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.GroupBoxAcquire.Size = new System.Drawing.Size(201, 222);
            this.GroupBoxAcquire.TabIndex = 6;
            this.GroupBoxAcquire.TabStop = false;
            this.GroupBoxAcquire.Text = "Acquire";
            // 
            // SaveBtn
            // 
            this.SaveBtn.Location = new System.Drawing.Point(59, 174);
            this.SaveBtn.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.SaveBtn.Name = "SaveBtn";
            this.SaveBtn.Size = new System.Drawing.Size(101, 31);
            this.SaveBtn.TabIndex = 5;
            this.SaveBtn.Text = "Save Data";
            this.SaveBtn.UseVisualStyleBackColor = true;
            this.SaveBtn.Click += new System.EventHandler(this.SaveBtn_Click);
            // 
            // Update_Renamed
            // 
            this.Update_Renamed.AutoSize = true;
            this.Update_Renamed.Location = new System.Drawing.Point(11, 140);
            this.Update_Renamed.Name = "Update_Renamed";
            this.Update_Renamed.Size = new System.Drawing.Size(31, 17);
            this.Update_Renamed.TabIndex = 4;
            this.Update_Renamed.Text = "N/A";
            // 
            // label20
            // 
            this.label20.AutoSize = true;
            this.label20.Location = new System.Drawing.Point(11, 121);
            this.label20.Name = "label20";
            this.label20.Size = new System.Drawing.Size(58, 17);
            this.label20.TabIndex = 3;
            this.label20.Text = "Update:";
            // 
            // StatusMessage
            // 
            this.StatusMessage.AutoSize = true;
            this.StatusMessage.Location = new System.Drawing.Point(11, 80);
            this.StatusMessage.Name = "StatusMessage";
            this.StatusMessage.Size = new System.Drawing.Size(31, 17);
            this.StatusMessage.TabIndex = 2;
            this.StatusMessage.Text = "N/A";
            // 
            // label19
            // 
            this.label19.AutoSize = true;
            this.label19.Location = new System.Drawing.Point(11, 60);
            this.label19.Name = "label19";
            this.label19.Size = new System.Drawing.Size(52, 17);
            this.label19.TabIndex = 1;
            this.label19.Text = "Status:";
            // 
            // StartBtn
            // 
            this.StartBtn.Location = new System.Drawing.Point(109, 20);
            this.StartBtn.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.StartBtn.Name = "StartBtn";
            this.StartBtn.Size = new System.Drawing.Size(71, 31);
            this.StartBtn.TabIndex = 0;
            this.StartBtn.Text = "Start";
            this.StartBtn.UseVisualStyleBackColor = true;
            this.StartBtn.Click += new System.EventHandler(this.StartBtn_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(561, 603);
            this.Controls.Add(this.GroupBoxAcquire);
            this.Controls.Add(this.GroupBoxStreamAcq);
            this.Controls.Add(this.GroupBoxCCDSetup);
            this.Controls.Add(this.GroupBoxCCDInfo);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.Name = "Form1";
            this.Text = "CCD Acquisition ( .NET C#)";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.groupBox1.ResumeLayout(false);
            this.GroupBoxCCDInfo.ResumeLayout(false);
            this.GroupBoxCCDInfo.PerformLayout();
            this.GroupBoxCCDSetup.ResumeLayout(false);
            this.GroupBoxCCDSetup.PerformLayout();
            this.groupBox4.ResumeLayout(false);
            this.groupBox4.PerformLayout();
            this.GroupBoxStreamAcq.ResumeLayout(false);
            this.GroupBoxStreamAcq.PerformLayout();
            this.GroupBoxAcquire.ResumeLayout(false);
            this.GroupBoxAcquire.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem mnuConfigure;
        private System.Windows.Forms.ToolStripMenuItem multiChannelDetectorToolStripMenuItem;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button CCD_InitializeBtn;
        private System.Windows.Forms.Button CCD_Connect;
        private System.Windows.Forms.ComboBox DeviceCombo;
        private System.Windows.Forms.GroupBox GroupBoxCCDInfo;
        private System.Windows.Forms.Label labelTempVal;
        private System.Windows.Forms.CheckBox checkTemp;
        private System.Windows.Forms.Timer timerTemperature;
        private System.Windows.Forms.GroupBox GroupBoxCCDSetup;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.RadioButton Image;
        private System.Windows.Forms.RadioButton Spectra;
        private System.Windows.Forms.ComboBox ADCSelect;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.ComboBox GainList;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label labelIntegrationTimeUnits;
        private System.Windows.Forms.TextBox IntTime;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox YStart;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox XStart;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox YEnd;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox XEnd;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox YBin;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.TextBox XBin;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Button SetParamsBtn;
        private System.Windows.Forms.GroupBox GroupBoxStreamAcq;
        private System.Windows.Forms.RadioButton Option3;
        private System.Windows.Forms.RadioButton Option2;
        private System.Windows.Forms.RadioButton Option1;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.TextBox Count;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.TextBox FileName;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.Button GoBtn;
        private System.Windows.Forms.GroupBox GroupBoxAcquire;
        private System.Windows.Forms.Label ChipY;
        private System.Windows.Forms.Label label17;
        private System.Windows.Forms.Label ChipX;
        private System.Windows.Forms.Label label15;
        private System.Windows.Forms.Label CCDName;
        private System.Windows.Forms.Label label14;
        private System.Windows.Forms.Label Description;
        private System.Windows.Forms.Label label18;
        private System.Windows.Forms.Label FWVersion;
        private System.Windows.Forms.Label label16;
        private System.Windows.Forms.Button SaveBtn;
        private System.Windows.Forms.Label Update_Renamed;
        private System.Windows.Forms.Label label20;
        private System.Windows.Forms.Label StatusMessage;
        private System.Windows.Forms.Label label19;
        private System.Windows.Forms.Button StartBtn;
        private System.Windows.Forms.Label label_IterationValue;
    }
}

