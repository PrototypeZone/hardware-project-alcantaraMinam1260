# Hardware report/Build instructions
Your target audience is a Computer Engineering Technology student from a different college that would like to recreate your project. Guidelines for next semester's CENG 355 Report are available.[^1]
[^1]: Technology Report Guidelines. OACETT, Revised September 2022. Available at: https://www.oacett.org/getmedia/5ad707d7-f472-4b24-a7fe-f34e270b0c41/2022_TR_Guidelines_-_Updated_Version_-_Sept_2022.pdf
## Table of Contents
[1.0 Introduction](#10-introduce-the-broadcom-development-platform-and-exisiting-functionality)   
[2.0 Body](#20-added-functionality)   
[2.1 Sensor/Effector purchase](#21-sensor-effector-purchase)   
[2.2 PCB design and soldering](#22-pcb-design-and-soldering)   
[2.3 Case design and assembly](#23-case-design-and-assembly)   
[2.4 Firmware development and use](#24-firmware-development-and-use)   
[3.0 Testing and Results](#30-testing-and-results)   
[4.0 References](#40-references)  

## 1.0 Sparkfun Qwiic Soil Moisture Sensor PI CENG-317 Project   

My name is Mi Nam Alcantara. This is a build instruction for my Pi Soil Moisture Sensor project. It uses Sparkfun’s SEN-17731 Qwiic Soil Moisture Sensor. Connected to a Raspberry Pi. This project will let the user measure the moisture levels for their potted plant/garden. 

![Finished](https://github.com/PrototypeZone/hardware-project-alcantaraMinam1260/blob/main/media/Finished.png)

__Specifications__

I2C address: (0x28)

Dimensions: 20.3x 100.0mm

## 2.0 Added functionality   

Completion of this project will net the user with a working soil moisture sensor. The sensor will measure the moisture levels with __1023__ being the highest moisture level and __1__ being the lowest moisture level

### 2.1 Sensor/Effector purchase   

Sensor:
SparkFun Qwiic Soil Moisture Sensor - https://www.sparkfun.com/products/17731

Bill of Materials for the other Project Items: 
https://github.com/PrototypeZone/hardware-project-alcantaraMinam1260/blob/main/hardware/bom.md

### 2.2 PCB design and soldering   

__PCB Creation__

1) Use KiCad

2) Launch KiCad and Start with default Settings

3) Download the below files:

[Project File](https://github.com/PrototypeZone/hardware-project-alcantaraMinam1260/blob/main/hardware/pcb/MiNamAlcantaraKiCad.kicad_pro)

[Schematic File](https://github.com/PrototypeZone/hardware-project-alcantaraMinam1260/blob/main/hardware/pcb/MiNamAlcantaraKiCad.kicad_sch)

[PCB File](https://github.com/PrototypeZone/hardware-project-alcantaraMinam1260/blob/main/hardware/pcb/MiNamAlcantaraKiCad.kicad_pcb)

4) Use KiCad to open the Project File

5) Edit the text of my name, and replace it with yours, and the date to the current date

6) Save Project As with your name and date

7) Use File->fabrication outputs->Gerbers (.gbr) and Plot the Gerbers

8) "Generate Drill Files"->PTH and NPTH in a single file

9) Save Project As with your name and date

10) Save it to a zip file

11) Print

__PCB Soldering__

Solder the PCB like below. Solder the resistors (220 ohm, 2.2k ohm), transistor (2N4124 PNP) and led (5mm LED). And solder the needed copper lines to the matching stacking header. __Perform a continuity test after soldering__.It follows the same layout as the KiCad PCB above.

![soldering](https://github.com/PrototypeZone/hardware-project-alcantaraMinam1260/blob/main/media/soldered_pcb.jpg) 

### 2.3 Case design and assembly   

__Case Design & Assembly__

1) Download the cdr file

2) Save as PDF

3) Print and Laser Cut the board

4) Unscrew the Rasberry Pi Shell if you have the shell on

5) Insert the M2.5 screw in to the 4 PI holes put the printed matching donut holes on top.

![screw](https://github.com/PrototypeZone/hardware-project-alcantaraMinam1260/blob/main/media/screw.JPG)

6) Insert the 16mm Standoff above

7) Place the PCB with the connected stacking header on top of the GPIO and 16mm Standoff respectively

8) Should look like below:

![standoff-header](https://github.com/PrototypeZone/hardware-project-alcantaraMinam1260/blob/main/media/standoff-header.JPG)

9) Plug the sensor the the Qwiic cables and plug it to the PCB Qwiic Outlet.

10) Finished Product should look like:

![Finished](https://github.com/PrototypeZone/hardware-project-alcantaraMinam1260/blob/main/media/Finished.png)


### 2.4 Firmware development and use   

__Firmware__

From the official sparkfun github account

[Firmware](https://github.com/sparkfun/Zio-Qwiic-Soil-Moisture-Sensor/tree/master/Firmware/Qwiic_Soil_Moisture_Sensor_Gateway_Firmware/Qwiic_Soil_Moisture_Firmware)

Updating firmware with the code above is not neccessary.

You can just connect the sensor to the Pi. And on putty type the following code:

pip install sparkfun-qwiic

This code should install the sparkfun libraries which will also contain the neccessary Qwiic Soil Moisture Sensor Libraries

## 3.0 Testing and Results   

Load Putty and sign in to the Pi. While the sensor is connected. 

Use i2cdetect -y 1 to scan for the Sensors I2C. if 28 pops up. The sensor is working properly, and cthere are no problems with the board. If not troubleshoot. Check PCB connections and check header GPIO,

![I2C](https://github.com/PrototypeZone/hardware-project-alcantaraMinam1260/blob/main/media/i2cdetect.png)

Upload my python code that I modified from the official sparkfun discord.

Make sure the code can be read and ran with chmod (And ends with .py).

Run the code with:

pyton "filename"

You should get results like below (depending on the moisture): 

![RESULT](https://github.com/PrototypeZone/hardware-project-alcantaraMinam1260/blob/main/media/result.png)

1023 is the Lowest Moisture Level

1 is the Highest Moisture Level

## 4.0 References   

Sparkfun - https://www.sparkfun.com/products/17731

Sparkfun Github - https://github.com/sparkfun/Zio-Qwiic-Soil-Moisture-Sensor/tree/master

Prototype Zone for some instructions - https://github.com/PrototypeZone/ceng317/tree/main/hardware/lasercutting






