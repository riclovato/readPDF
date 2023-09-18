$exclude = @("venv", "readPDF.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "readPDF.zip" -Force