## Get your owned gog games into a json file

virtualenv3 venv3
source venv3/bin/activate

pip install https://github.com/Yepoleb/pygogapi/archive/master.zip

first run auth.py and follow the instructions

then run python getgames.py to create owned.json

Also goto `https://www.gog.com/account` in your browser press `F12` and run following snipet in the console.

```
document.write(JSON.stringify(gogData.accountProducts.map(p=>({id: p.id,image:p.image+"_392.jpg",title:p.title,url:p.url}))))
```

and paste the resulting text in a second output file, name is up to your choice