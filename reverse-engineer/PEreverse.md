PE reverse
====

The Portable Executable (PE) format is a file format for executables, object code, DLLs, FON Font files,[1] and others used in 32-bit and 64-bit versions of Windows operating systems.

Tools
----

 - Ollydbg for rdebugging assembly
 - PEstudio for static analysis
 - RessourceHacker for more advance static analysis

How to
---

Before running the executable file into Ollydbg, make a static analysis with PEStudio. what you are usually trying to find is Resource and Symbols. Resource can contains files or other executable while Symbols might contains callable function.

DLL
----

To run a dll, windows has an utility called `rundll32`. You can call function from within the DLL like this : `rundll32 my.dll,FunctionCall`.
