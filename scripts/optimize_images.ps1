# Shrink the large images used by the static site (site/assets/images).
# Uses System.Drawing, which ships with Windows PowerShell 5.1, so nothing is installed.
# Photos become JPEG (quality 82), the logo and the illustration stay PNG so transparency survives.
Add-Type -AssemblyName System.Drawing

$dir = Join-Path (Split-Path $PSScriptRoot -Parent) 'site\assets\images'
$jpegCodec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
$jpegParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
$jpegParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, 82L)

function Resize-Image([string]$name, [int]$maxWidth, [string]$outName, [bool]$asJpeg) {
    $src = Join-Path $dir $name
    $dst = Join-Path $dir $outName
    $img = [System.Drawing.Image]::FromFile($src)
    try {
        $ratio = [Math]::Min(1.0, $maxWidth / $img.Width)
        $w = [int]($img.Width * $ratio); $h = [int]($img.Height * $ratio)
        $bmp = New-Object System.Drawing.Bitmap($w, $h, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
        $g = [System.Drawing.Graphics]::FromImage($bmp)
        $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
        if ($asJpeg) { $g.Clear([System.Drawing.Color]::White) }
        $g.DrawImage($img, 0, 0, $w, $h)
        $g.Dispose()
        $tmp = "$dst.tmp"
        if ($asJpeg) { $bmp.Save($tmp, $jpegCodec, $jpegParams) } else { $bmp.Save($tmp, [System.Drawing.Imaging.ImageFormat]::Png) }
        $bmp.Dispose()
    } finally { $img.Dispose() }
    Move-Item -Force $tmp $dst
    "{0} -> {1} ({2:N0} KB)" -f $name, $outName, ((Get-Item $dst).Length / 1KB)
}

Resize-Image 'thaco-le-trao-chia-khoa.png' 1600 'thaco-le-trao-chia-khoa.jpg' $true
Resize-Image 'bao-hiem-hang-hoa-1.png' 1000 'bao-hiem-hang-hoa-1.jpg' $true
Resize-Image 'bao-hiem-hang-hoa-2.png' 1000 'bao-hiem-hang-hoa-2.jpg' $true
Resize-Image 'ptdl-logo.png' 176 'ptdl-logo.png' $false
Resize-Image 'van-chuyen-quoc-te.png' 900 'van-chuyen-quoc-te.png' $false
