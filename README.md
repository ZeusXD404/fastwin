# fastwin<br>
## DISCLAIMER:
<code>I DO NOT ENCOURAGE ABUSING GITHUB ACTIONS IN ANY WAY. THIS IS AN EDUCATIONAL
GUIDE HELPING THOSE WHO WANT TO TRY TOOLS LIKE VISUAL STUDIO AND OTHERS WITHIN A 
FULL FLEDGED EPHEMERAL WINDOWS VM. PLEASE DO NOT MISUSE RESOURCES.</code><be>
## Steps To Setup:
- Fork this repo, and continue there.
- Signup at [ngrok](https://ngrok.com/) and get your authtoken.
- Setup a bot on [telegram](https://t.me/BotFather) and get your bot API token.
- Add two secrets to your forked repo namely:
  - <code>NGROK_AUTH_TOKEN</code> with the value being your ngrok authtoken.
  - <code>BOT_TOKEN</code> with the value being your bot API token.
- Open the file named <code>tunnel_info.py</code> and search for <code>chat_id</code>
string. Edit the value with your userid on telegram.
- Send any message to the bot you made. Come back here and open <code>Actions</code> tab.
- Select <code>windows</code> workflow and then <code>run workflow</code>.
- If everything is alright, the RDP access IP will be sent to you over telegram within 1-2 minutes.
- You can also check the <code>Actions</code> tab for logs.<br>
## RDP Credentials:
- Username: <code>runneradmin</code>
- Password: <code>P@ssw0rd!</code><br>
## Tips and Tricks:
- The RDP will be running for 6hours at max. Don't close the CMD window running by default
when you login as it can kill the session.
- Message [IDBot](https://t.me/myidbot) on telegram, to know your userid.
- Read this [guide](https://docs.github.com/en/actions/reference/encrypted-secrets) to know how 
to add secrets to your repo.
- Try to avoid running highly CPU or Memory intensive tasks as it has a high potential to kill your
session.
- You CANNOT provision more than one VM session at a time, it will fail.
- Either cancel the workflow from <code>Actions</code> tab or poweroff the VM when you are done, 
so as to save resources.
- Whenever you need a session just go to <code>Actions</code> tab and <code>run workflow</code>.
