from __future__ import absolute_import, print_function

from ScopeFoundry import HardwareComponent
from Hardware.horiba_ccd import horiba_ccd
#from pyqtgraph.parametertree.parameterTypes import str



class horiba_ccd_hc(HardwareComponent):
    
    name = "Horiba Synercity CCD"
    
    def setup(self):
        self.debug = False
               
        self.settings.New(
                                name="dev_name",
                                dtype=str,
                                initial="CCD1",
                                reread_from_hardware_after_write=False)
        self.settings.New(
                                name='integration',
                                dtype=float,
                                ro = False,
                                unit="s",
                                vmin=0, vmax=30e3,
                                spinbox_decimals = 3,
                                reread_from_hardware_after_write = False
                            )
        
        self.settings.New(
                                name='temperature',
                                dtype=float,
                                ro = True,
                                unit="K",
                                vmin=0, vmax=30e3,
                                spinbox_decimals = 3,
                                reread_from_hardware_after_write = True
                            )
        
        self.settings.New(
                                name='temperature_setpoint',
                                dtype=float,
                                ro = False,
                                unit="K",
                                initial=290,
                                vmin=200, vmax=350,
                                spinbox_decimals = 3,
                                reread_from_hardware_after_write = True
                            )
        
        self.settings.New(
                                name = 'acq_mode',
                                dtype=str,
                                choices = [('Image','image'),
                                           ('Single Track', 'single_track'),
                                           ('Full Vertical Binning', 'fvb')]                                
                            )
        
        self.settings.New(
                                name = 'adc',
                                dtype=int,
                                choices = [('',-1)]                                
                            )
        
        self.settings.New(
                                name = 'gain',
                                dtype=int,
                                choices = [('',-1)]                                
                            )
        
        self.settings.New(
                                name="roi_start_x",
                                dtype=int, 
                                ro = False,
                                spinbox_decimals=0, 
                                reread_from_hardware_after_write = False
                            )
        
        self.settings.New(
                                name="roi_start_y",
                                dtype=int, 
                                ro = False,
                                spinbox_decimals=0, 
                                reread_from_hardware_after_write = False
                            )
        
        self.settings.New(
                                name="roi_width",
                                dtype=int, 
                                ro = False,
                                spinbox_decimals=0, 
                                reread_from_hardware_after_write = False
                            )
        
        self.settings.New(
                                name="roi_height",
                                dtype=int, 
                                ro = False,
                                spinbox_decimals=0, 
                                reread_from_hardware_after_write = False
                            )
                
        self.settings.New(
                                name="bin_size_x",
                                dtype=int, 
                                ro = False,
                                spinbox_decimals=0, 
                                reread_from_hardware_after_write = False
                            )
        
        self.settings.New(
                                name="bin_size_y",
                                dtype=int, 
                                ro = False,
                                spinbox_decimals=0, 
                                reread_from_hardware_after_write = False
                            )
        
        self.settings.New(
                                name = "hflip",
                                dtype = bool,
                                ro = False,
                                initial=True    
                            )
        
        self.settings.New(
                                name = "acq_busy",
                                dtype = bool,
                                ro = True,    
                            )
        
        
        
        
    def connect(self):
        if self.debug: self.log.info( "connecting to horiba CCD camera" )

        # Open connection to hardware
        c = self.cam = horiba_ccd()
        
        # Get the device name from the logged quantity
        dev_name = self.settings.dev_name.value
        
        c.open_camera(dev_name)
        
        # Connect the logged quantities
        
        # Integration time
        self.settings.integration.connect_to_hardware(
            read_func=c.get_integration_time,
            write_func=c.set_integration_time)
        
        # Acquisition mode
        self.settings.acq_mode.connect_to_hardware(
            read_func = c.get_acquisition_mode,
            write_func = c.set_acquisition_mode)
        
        # Device temperature
        self.settings.temperature.connect_to_hardware(
            read_func = c.get_temperature,
            write_func = None)
        
        # Temperature setpoint
        self.settings.temperature_setpoint.connect_to_hardware(
            read_func = c.get_temperature_setpoint,
            write_func = c.set_temperature_setpoint)
        
        # ADC settings
        adc_choices =[(a[1], a[0]) for a in c.adc_settings]
        self.settings.adc.change_choice_list(adc_choices)
        
        self.settings.adc.connect_to_hardware(
            read_func = c.get_adc,
            write_func = c.set_adc)
        
        # Gain settings
        gain_choices =[(g[1], g[0]) for g in c.gain_settings]
        self.settings.gain.change_choice_list(gain_choices)
        
        self.settings.gain.connect_to_hardware(
            read_func = c.get_gain,
            write_func = c.set_gain)
        
        self.settings.hflip.connect_to_hardware(
            read_func=c.get_hflip,
            write_func=c.set_hflip)        
        
        self.settings.acq_busy.connect_to_hardware(
            read_func = c.get_acquisition_busy,
            write_func = None)
        
        c.dump_settings()
        
        self.read_from_hardware()


    def disconnect(self):
        self.log.info( "disconnect " + self.name )
        
        #disconnect logged quantities from hardware
        self.settings.disconnect_all_from_hardware()
        
        
        if hasattr(self, 'cam'):
            #disconnect hardware
            self.cam.close_camera()
            
            # clean up hardware object
            del self.cam

