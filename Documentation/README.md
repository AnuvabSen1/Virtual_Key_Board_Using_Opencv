<div align="center">
<img src="https://i.pinimg.com/736x/8c/7d/7b/8c7d7ba18c6d31e7883dec925eec874e.jpg" alt="Akeno" width="500" />

# **Anuvab Bot**

Anuvab is a multipurpose WhatsApp bot using wa-automate-nodejs library!
>
>

<p align="center" style="display: inline">
 <img src="https://img.shields.io/github/followers/AnuvabSen?style=for-the-badge">
<img src="https://img.shields.io/github/stars/AnuvabSen?style=for-the-badge">
<a href="https://www.linkedin.com/in/anuvab-sen-316383202"><img src="https://img.shields.io/badge/-Anuvab-blue?style=for-the-badge&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/anuvab-sen-316383202/)](https://www.linkedin.com/in/anuvab-sen-316383202"></a>
</p>

  
<p align="center">
  <a href="https://github.com/Jazzboy-12/Anuvab-Whatsapp-Bot#requirements">Requirements</a> •
  <a href="https://github.com/Jazzboy-12/Anuvab-Whatsapp-Bot#installation">Installation</a> •
  <a href="https://github.com/Jazzboy-12/Anuvab-Whatsapp-Bot#features">Features</a> •
  <a href="https://github.com/Jazzboy-12/Anuvab-Whatsapp-Bot#original-authors ">Thanks to</a>
</p>

</div>

# Requirements
* [Node.js](https://nodejs.org/en/)
* [Git](https://git-scm.com/downloads)
* [FFmpeg](https://www.gyan.dev/ffmpeg/builds/)
* [Tesseract](https://s.id/vftesseract)
* [ImageMagick](https://imagemagick.org/script/download.php)
* [gif2webp](https://developers.google.com/speed/webp/download)
* Any text editor

# Installation
## 📝 Cloning this repo
```cmd
> git clone https://github.com/Jazzboy-12/Anuvab-Whatsapp-Bot.git
> cd Anuvab-Whatsapp-Bot
```

## ✍️ Editing the file
Edit `config.json` to customize the bot as needed
```JSON

{
    "botadmins": ["9433148854@c.us"],
    "prefix": "~",
    "uaOverride": "WhatsApp/2.2037.6 Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "botname": "Anuvab"
}

```

`botadmins`: Put the array of [contactIds](https://docs.openwa.dev/globals.html#contactid) of the people who you want be bot admins <br>
`prefix`: The prefix of the bot <br>
`uaOverride`: Your user Agent<br>
`botname`: The name of your bot<br>

Edit `help.js` for bot name and display messages

## 🧾 Installing the Tesseract
* Download the file [here](https://s.id/vftesseract).
* After that, run downloaded file as Administrator.
* Complete the installation.
* Run Command Prompt as Administrator.
* Run this command:
```cmd
> setx /m PATH "C:\Program Files\Tesseract-OCR;%PATH%"
```
It will give us a callback like `SUCCESS: specified value was saved`.
* Now that you've Tesseract installed, verify that it's working by running this command to see version number (may need to restart Command Prompt):
```cmd
> tesseract -version
```

## 🛠️ Installing the FFmpeg
* Download one of the available versions of FFmpeg by clicking [this link](https://www.gyan.dev/ffmpeg/builds/).
* Extract the file to `C:\` path.
* Rename the extracted folder to `ffmpeg`.
* Run Command Prompt as Administrator.
* Run this command:
```cmd
> setx /m PATH "C:\ffmpeg\bin;%PATH%"
```
It will give us a callback like `SUCCESS: specified value was saved`.
* Now that you've FFmpeg installed, verify that it's working by running this command to see version number (may need to restart Command Prompt):
```cmd
> ffmpeg -version
```

## 🕸 Installing the gif2webp
* Download one of the available versions of gif2webp by clicking [this link](https://developers.google.com/speed/webp/download).
* Extract the file to `C:\` path.
* Rename the extracted folder to `libwebp`.
* Run Command Prompt as Administrator.
* Run this command:
```cmd
> setx /m PATH "C:\libwebp\bin;%PATH%"
```
It will give us a callback like `SUCCESS: specified value was saved`.
* Now that you've gif2webp installed, verify that it's working by running this command to see version number (may need to restart Command Prompt):
```cmd
> gif2webp -version
```

## 🔍 Installing the dependencies
```cmd
> npm install
```

## 🆗 Running the bot
Regular node:
```cmd
> npm start
```

PM2:
```cmd
> pm2 start index.js
> pm2 monit
```

PM2 with cron job (restart after 5 hours):
```cmd
> pm2 start index.js --cron "* */5 * * *"
> pm2 monit
```

After that scan the QR code using your WhatsApp in your phone!

# Features

### Prefix = !

| Features                           | Command           | Acces    |
|:----------------------------------:|:-----------------:|:--------:|
| Convert Images/Gifs into stickers  | !sticker          | Everyone |
| Gives Caption to Images and converts them into stickers  | !stickermeme          | Everyone |
| Triggers Images and converts them into stickers  | !triggered          | Everyone |
| Converts stickers to images  | !toimg          | Everyone |
| GTA styled wasted caption to images  | !wasted          | Everyone |
| Display anime info                 | !anime <anime name> | Everyone |
| Display Group info                 | !groupinfo        | Everyone |
| Return anime wallpapers                  | !wallpaper <term>   | Everyone |
| Scrap Subreddits [image based]     | !sr subreddit     | Everyone |
| Display Covid 19 Info              | !covid country    | Everyone | 
| Don't know why I did that              | !kissu    | Everyone | 
| Returns pornhub styled comment              | !phcomment <Name | comment>   | Everyone | 
| Toggle NSFW                        | !act nsfw         | Admins   |
| Greet new members                  | !act welcome      | Admins   |
| Mention all group members          | !ping text        | Admins   |
| Promote members                    | !promote @user    | Admins   |
| Demote admins                      | !demote @user     | Admins   |
| Display User profile               | !profile / !profile @user          | Everyone |
| Kicks the user               | !snap @user          | Admins |
| Bot leaves the group               | !leave          | Admins |
| Bot joins using group invite link               | !join <link>         | Bot Admin |
| Sets status of Anuvab              | !setstatus        | Bot Admin |
| Gives english text from image               | !ocr          | Everyone |
| Broadcasts messages to all chats of Anuvab            | !bc          | Bot Admin |

### Random results

| Command | Result |
|:-------:|:------:|
|!pokemon <pokemon name> | Displays a random pokemon|
|!rpaper  | Displays a random Wallpaper|
|!waifu   | Displays a random waifu and the info |
|!husbu / !husbando   | Displays a random husbando and info |
|!animeneko | Displays a random animeneko |
|!cat     | Displays a random cat |
|!doggo    | Displays a random dog |
|!dogesticker    | Displays a random doge sticker |
|!wholesome    | Displays a random wholesome sticker |
|!animesticker    | Displays a random anime character sticker |
|!tod            | Truth or dare game |
|!pickup            | Pickup lines |


## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/AnuvabSen/Anuvab-Whatsapp-Bot). 

# Anuvab-Whatsapp-Bot

  
