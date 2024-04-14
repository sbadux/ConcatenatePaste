# ConcatenatePaste
 Simple python tool to concatenate strings with AND/OR.
 On Windows, it creates a system tray icon where you can select the conjunction to concatenate all the rows copied in the clipboard

## Disclaimer
I'm not a developer so the code of this project is probabily ugly, but it works.
I just want to share this little script I use for my personal needs hoping it can be useful to someone else.
Feel free to fork, improve or give me any suggestion for improving the code. It will be welcome.

## How to use it
It opens up as a system tray icon. By right-clicking the icon you can select the conjunction you prefer to concatenate strings.

![immagine](https://github.com/sbadux/ConcatenatePaste/assets/28478027/3ddb8469-db0f-4ef7-b413-65da1a788712)

If you have any kind of list, like this one:

1987Dsd

1999d dhs21

1774name7

1826dhey11

858ptrg5


just copy the list and select the conjuction you need.
Your clipboard will be automatically filled with the concatenated text and you can immediately paste it where needed


If you select **OR**:
1987DSD OR 1999DDHS21 OR 1774NAME7 OR 1826DHEY11 OR 858PTRG5


If you select **AND**:
1987DSD AND 1999DDHS21 AND 1774NAME7 AND 1826DHEY11 AND 858PTRG5


If you select **AND <>**:
<>1987DSD AND <>1999DDHS21 AND <>1774NAME7 AND <>1826DHEY11 AND <>858PTRG5


## Settings
ConcatenatePaste has few settings at the moment:

**All Capitals** 

Enabled by default, all the copied text is forced in capital letters (see the example in the previous section).
Disabling this flag the text is kept in his original state.
Eg: 1987Dsd* OR 1999ddhs21* OR 1774name7* OR 1826dhey11* OR 858ptrg5*

**Remove spaces**

Enabled by default, it removes spaces and tabulations.
If the copied list contains a value like this "1999d dhs21" it will be automatically concatenated as "1999ddhs21" unless you uncheck the "Remove spaces" option.

**Front asterisk**

Disabled by default, it adds an asterisk as first charachter.
Eg: 1999ddhs21 will be concatenated as "1999ddhs21" by default, or `*1999ddhs21` if the option is enabled

**End asterisk**

Enabled by default, it adds an asterisk as last charachter.
Eg: 1999ddhs21 will be concatenated as "1999ddhs21*" by default, or `1999ddhs21` if the option is disabled


## Next steps
- I will like to make ConcatenatePaste able to remember the last settings, but I'm not enough expert in delevoping.
I will try to figure out how to do it in the future, but I also like the fact that this tool does *absolutely nothing* on the PC where it is run. It just runs and doesn't write a single file.
