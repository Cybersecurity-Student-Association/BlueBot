import { Client, GatewayIntentBits, InteractionType } from "discord.js";
import registeredCommands from "./registeredCommands.js";
import Parser from "rss-parser";

const client = new Client({ 
    intents: [ 
        GatewayIntentBits.Guilds, 
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.GuildMembers
    ],
    partials: ['MESSAGE', 'CHANNEL', 'REACTION'],
});

client.once('ready', async () =>  {
    console.log("BlueBot has logged in.");
    client.user.setPresence({ activities: [{ name: 'I\'m blue, da ba dee da ba di' }] });
    console.log("Registering discord commands.");
    registeredCommands.forEach(async command => {
        await client.application.commands.create(command.body.toJSON(), process.env.PROD ? undefined : process.env.GUILD);
    });

    let parser = new Parser();
    let feed = await parser.parseURL("http://lorem-rss.herokuapp.com/feed");
    console.log(feed.title);

    const rssChannel = client.channels.cache.get("1112401885979222068");
    feed.items.forEach(item => {
        rssChannel.send(`New Update: ${item.title} - ${item.link}`);
    });
    // Testing

    client.on('interactionCreate', async interaction => {
        if (interaction.type != InteractionType.ApplicationCommand) return;
        const { commandName } = interaction;
        //We do another forEach here instead of checking in the above foreach
        //The interactionCreate was run with each command before, causing memory issues
        registeredCommands.forEach(async command =>  {
        if (commandName === command.body.name) {
            await command.onTriggered(interaction);
        }
    });
    });
    client.on('messageCreate', message => {
        if (message.mentions.users.get('1112401613408182322') && !message.author.bot) {
           message.reply("Don't @ me.");
           }
        if (message.content.toLowerCase() === 'inertia') {
           message.reply('Inertia is a property of matter.');
           }
    });
    client.on('guildMemberAdd', async (member)=> {
        await member.guild.channels.cache.get('1112401885979222068').send({ files: ['./assets/CS2A.png'] });
        await member.guild.channels.cache.get('1112401885979222068').send(`Welcome <@`+member.user.id+`>!\nPlease change your nickname to include your real name and make sure to officially join the club on Campus Groups (link found in <#779793774628175892>).`)
    });
    console.log("Discord commands registered, BlueBot is ready for use.")
});

export default client;