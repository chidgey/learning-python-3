# Graphical Catalog Utility

Use this utility to create the stucture for a graphic design catalogue where
you can easily store client work, shared art, icons, fonts etc... under a common
structure format.

This makes it easier to merge this work with the cloud and share across different
devices as you are on the move.

## Usage
gdcu init - initiaises the current folder as a design catalogue and sets up shared
folders, readme files etc...

    e.g. 
        mkdir GraphicDesignWork
        cd GraphicDesignWork
        gdcu init

        ...
        /GraphicDesignWork/
        /GraphicDesignWork/Shared/Fonts/
        /GraphicDesignWork/Shared/Illustrations/
        /GraphicDesignWork/Shared/Brushes
        Done!

### Adding a new client
Adds a new client folder that will contain various projects.

```bash
python gcu add client "Emergent Software Ltd" 
```
### Adding a new project
Adds a new project, note that you need to be in a client folder to run this command.
```bash
python gcu add project "Launch Campaign"
```
### 
 - adds a new project for the client
e.g.  /GraphicDesignWork/001_Emergent_Software_Ltd/Launch_Campaign

### Analysing your projects (experimental)
Using the Google vision API to examine images and metadata label them for easier
finding later.
```
gcu analyze 
```

## Future work

- [ ] Use the colorama module to bring colours into the command line. pip install colorama