# dotman

*This repository is a work in progress.*

This program aims to manage your dotfiles in a way similar to [GNU Stow](https://www.gnu.org/software/stow/). However, the goal is for the "stowed" files to be templates which are modified by **filters**. In fact, the main feature of stow -- creating the symlinks -- is implemented with a filter. These filters can be written in any language granted that they are exectuable. This standard would allow for infinite extensibility from a relatively simple base.

The current implemented features are
* A configuration file - the default can be changed at runtime
* A defined package structure
* Subcommands:
  * `add` - moves a dotfile to a managed package
  * `update` - applies filters to a package
  * `init` - sets up base configuration

This project is currently on hold but I hope to complete it and fully document it soon.
