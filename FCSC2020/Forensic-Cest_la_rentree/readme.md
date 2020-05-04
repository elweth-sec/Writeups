
```powershell
strings dmp.mem | grep hostname
..... challenge.fcsc .....
strings dmp.mem | grep "-amd"
..... Linux 5.4.0-4-amd64 .....
strings dmp.mem | grep "/home/"
..... Lesage .....
```
FCSC{challenge.fcsc:Lesage:5.4.0-4-amd64}
