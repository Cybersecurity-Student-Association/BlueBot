import { SlashCommandBuilder } from '@discordjs/builders';
import { EmbedBuilder } from 'discord.js';




export default {
    body: new SlashCommandBuilder()
        .setName('createevent')
        .setDescription('Creates a reaction-joinable event and thread.')
        .addStringOption(option =>
            option.setName('name')
                .setDescription('Name of the event.')
                .setRequired(true)
                .addChoices(
                    { name: 'Roles', value: 'roles' },
                    { name: 'Rules', value: 'rules' },
                    { name: 'Club Info', value: 'clubinfo' },
                ))
        .setDefaultMemberPermissions(0)
        .setDMPermission(false),
    onTriggered: async function(interaction) {
        let cs2alogourl = 'https://raw.githubusercontent.com/Cybersecurity-Student-Association/BlueBot/main/assets/CS2A.png';
        let cs2acgurl = 'https://raw.githubusercontent.com/Cybersecurity-Student-Association/BlueBot/main/assets/CS2A_cg.png';
        const embed = interaction.options.getString('name')
        if (embed == 'roles') {
            const embed = new EmbedBuilder()
            .setTitle('CS2A Discord Roles')
            .setColor('#1b2956')
            .setFooter({text:'BlueBot | Made by CS2A Bot Developers', iconURL:cs2alogourl})
            .setThumbnail(cs2alogourl)
            .addFields(
             {name: 'Admin & Officer Roles',
             value: 
             `<@698223788654985217>: Admins for this Discord server
             <@492041240649662466>: Oversees the club (also the person who pings everyone)
             <@979757997700042752>: VP, Treasurer, & Secretary, handle club administration
             <@492040980510408704>: Club officers, help with club operations, moderators for the discord server, ping for club questions or if you need assistance
             `},
             {name: 'Special Roles',
             value: 
             `These roles are given to special people or for activities.
             <@745814798419230740>: the machines
             <@1097921051289190503>: Build and maintain *the machines*
             <@698215508503167026>: ODU personnel
             <@979061709392187442>: Gives access to the active events channel
             `},
             {name: 'Cosmetic Roles',
             value: 
             `You can get these roles in the Channels & Roles at the top of the server navigation.
             `},
             {name: 'Accomplishments',
             value: 
             `<@680978070202613760>: You graduated from ODU!
             <@492040852797915157>: You earned the Security+ certification!
             `},
             {name: 'Majors',
             value: 
             `<@1060958866243866635>: Cyber-Security Major
             <@831307965717413908>: Cyber-Operations Major
             <@1062400799650631770>: Computer Science Majors
             <@1062401293743825056>: Engineer Majors
             `},
             {name: 'For fun',
             value: 
             `<@745829275076395059>: Cyber defense
             <@745829089646215269>: Cyber offense
             `},
                      )
            interaction.channel.send({embeds:[embed]});
            interaction.reply({content: `Embed posted.`,ephemeral: true})
        }
        if (embed == 'rules') {
            const embed = new EmbedBuilder()
            .setTitle('CS2A Discord Rules')
            .setColor('#1b2956')
            .setFooter({text:'BlueBot | Made by CS2A Bot Developers', iconURL:cs2alogourl})
            .setThumbnail(cs2alogourl)
            .addFields(
             {name: ':one: Be Respectful',
             value: 
             `You must respect all users regardless of your liking towards them. We encourage constructive discourse.
             `},
             {name: ':two: Tolerance',
             value: 
             `No homophobia, racism, sexism, slurs, or discrimination/bias of any from.
             `},
             {name: ':three: Do not Spam',
             value: 
             `Do not send a lot of small messages right after each other. Do not disrupt chat by spamming.
             `},
             {name: ':four: No NSFW Material',
             value: 
             `This is a community server, not the place for that type of content.
             `},
             {name: ':five:  Names and Profile Pictures',
             value: 
             `No offensive nicknames or profile pictures. 
             Real Name policy: This server has a real name policy. If you still want your user name displayed simply add your first name to the front it.
             `},
             {name: ':six: Direct and Indirect Threats',
             value: 
             `Threats against other users (Death, DDoS, DoX, abuse, and malicious threats) will not be tolerated.
             `},
             {name: ':seven: Follow the Discord Community Guidelines',
             value: 
             `You can find those here https://discord.com/new/guidelines.
             `},
             {name: ':eight: Follow the ODU Student Code of Conduct',
             value: 
             `You can find those here:
             https://www.odu.edu/content/dam/odu/offices/bov/policies/1500/BOV1530.pdf.

             Please limit any political discourse to topics directly related to cyber only.
            If you see something against the rules or something that makes you feel unsafe, let an officer know. We want this server to be a welcoming space!
            The Admins may Kick/Ban at their discretion. If you feel there was error, please contact an Admin.
             `},
                      )
            interaction.channel.send({embeds:[embed]});
            interaction.reply({content: `Embed posted.`,ephemeral: true})
        }
        if (embed == 'clubinfo') {
            const embed = new EmbedBuilder()
            .setTitle('CS2A Club Info')
            .setColor('#1b2956')
            .setFooter({text:'BlueBot | Made by CS2A Bot Developers', iconURL:cs2alogourl})
            .setThumbnail(cs2alogourl)
            .addFields(
             {name: 'Server Invite',
             value: 
             `https://discord.gg/aGG4Zjt 
             `},
             {name: 'Join the CS2A Campus Groups',
             value: 
             `https://odu.campusgroups.com/cs2a/club_signup
             `},
                      )
            .setImage(cs2acgurl)
            interaction.channel.send({embeds:[embed]});
            interaction.reply({content: `Embed posted.`,ephemeral: true})
        }
    }   
};
