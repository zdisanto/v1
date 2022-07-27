
<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>CS1</title>
    <link href="../CS1.css" rel="stylesheet" type="text/css">
</head>

<body>

  <div class="container">

    <div class="block">
      <h1>WordsList(Array) Demo</h1>
      <p>
	The following text was written to the standard output stream when the <tt>WordsList.html</tt> program was executed from IntelliJ.
      </p>
      <div class="block">
	<h2></h2>
	<p>
	  <pre>
>>> help
HELP - display a menu of commands
DISPLAY - display the list of words
PRINT - print a word (FIRST;LAST;nth)
SWAP - exchange two elements (nth;mth)
ADD - add a word to the list (FIRST;LAST)
EXIT - terminate execution of the program
>>> display
Epiphany
Resol
Sonder
Flaccid
Aurora
Ethereal
Passion
Ignite
Oblivion
Nocturnal
>>> print first
Epiphany
>>> print last
Nocturnal
>>> print 4
Flaccid
>>> print 9
Oblivion
>>> swap 4 8
>>> display
Epiphany
Resol
Sonder
Ignite
Aurora
Ethereal
Passion
Flaccid
Oblivion
Nocturnal
>>> add first hello
>>> display
hello
Epiphany
Resol
Sonder
Ignite
Aurora
Ethereal
Passion
Flaccid
Oblivion
Nocturnal
>>> add last goodbye
>>> display
hello
Epiphany
Resol
Sonder
Ignite
Aurora
Ethereal
Passion
Flaccid
Oblivion
Nocturnal
goodbye
>>> exit
	  </pre>
	</p>
      </div>
    </div>

  </div>

</body>
</html>
