set -e
cd `dirname $0`

FILE_PATH="$HOME/Pictures/random.png"

if [ $# -ne 1 ]; then
    echo "usage: wallpaper.sh <url>"
    exit 1
fi

url=$1
curl -L -o $FILE_PATH $url
osascript wallpaper.js $FILE_PATH
killall Dock
