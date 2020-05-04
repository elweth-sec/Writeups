To get the flag, we have to bypass this condition: 

```powershell
if(md5($_GET['secret']) == $_GET['secret'])
```

So we need to find : md5(x) == x

And md5(0e215962017) == 0e215962017

So we get the flag

FCSC{f67aaeb3b15152b216cb1addbf0236c66f9d81c4487c4db813c1de8603bb2b5b}
