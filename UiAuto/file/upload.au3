ControlFocus("��","","Edit1");
WinWait("CLASS:#32770","",10);
ControlSetText("��","","Edit1",$CmdLine[1]);
sleep(2000);
ControlClick("��","","Button1");
sleep(2000);