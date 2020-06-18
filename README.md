# CamControlHub
  
#### This is currently used in a misterious lab only.

### Introduction

This is used as a Camera Contoller Hub. The repo is composed of software-side (in Python 3.8) and hardware-side (with Arduino). The system can control a group of DSLR cameras and capture images one by one or simultaneously.
  
### Features

- Python tkinter GUI
- Arduino pin config: pulled up and ground to trigger
- Configurable frame-rate
- When capturing in turn, a new round can be added at any time (minimal interval depended on cameras)
  
### Installation

Download the codes, upload ino to Arduino Mega 2560 (may need C340 or other drivers depending on your device), install PySerial library, and enjoy.
  
### Feedback

Contact wangyw.dev@outlook.com
