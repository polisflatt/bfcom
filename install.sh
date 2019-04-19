
if [ ! -e /usr/bin/bfcomdir/ ]; then
    mkdir /usr/bin/bfcomdir/
fi

cp -r * /usr/bin/bfcomdir/


if [ -e /usr/bin/bfcom ]; then
    rm /usr/bin/bfcom
fi

ln -s /usr/bin/bfcomdir/main.py /usr/bin/bfcom
chmod 777 /usr/bin/bfcom

echo "Done."