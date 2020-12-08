## Get your owned gog games into a json file

first time setup:
```sh
virtualenv3 venv3
source venv3/bin/activate

pip install https://github.com/Yepoleb/pygogapi/archive/master.zip

# first run auth.py and follow the instructions:
python auth.py
```

then run `python getgames.py` to create owned.json

Also goto `https://www.gog.com/account` in your browser press `F12` and run following snipet in the console.

```
document.write(JSON.stringify(gogData.accountProducts.map(p=>({id: p.id,image:p.image+"_392.jpg",title:p.title,url:p.url}))))
```

and paste the resulting text in a second output file, name is up to your choice


you can get only the gamenames from the `owned.json` file with `jq`:

```sh
cat owned.json | jq -r '(.data)| .[] | select(.title).title'
```