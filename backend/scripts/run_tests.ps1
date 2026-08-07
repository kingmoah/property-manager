$log = ".\backend\scripts\test.log"

"========================================" >> $log
"Test Run: $(Get-Date)" >> $log
"========================================" >> $log

.\backend\scripts\api_test.ps1 *>&1 |
    Tee-Object -FilePath $log