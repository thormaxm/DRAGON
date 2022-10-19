if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/thormaxm/DRAGON.git /DRAGON
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /DRAGON
fi
cd /DRAGON
pip3 install -U -r requirements.txt
echo "⚡DRAGON Starting Bot⚡...."
python3 bot.py
