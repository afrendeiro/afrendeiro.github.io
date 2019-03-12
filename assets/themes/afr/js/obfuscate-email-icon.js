<!--
// Email obfuscator script 2.1 by Tim Williams, University of Arizona
// Random encryption key feature by Andrew Moulden, Site Engineering Ltd
// This code is freeware provided these four comment lines remain intact
// A wizard to generate this code is at http://www.jottings.com/obfuscator/
{ coded = "3p8lqKl18G@N731v.eG7"
  key = "ruCKWhylzA6QNqU1YaRV89DXZ0BvOcsk2jSxt3omfFwEIdbTJeMPHLgn4iG7p5"
  shift=coded.length
  link=""
  for (i=0; i<coded.length; i++) {
    if (key.indexOf(coded.charAt(i))==-1) {
      ltr = coded.charAt(i)
      link += (ltr)
    }
    else {     
      ltr = (key.indexOf(coded.charAt(i))-shift+key.length) % key.length
      link += (key.charAt(ltr))
    }
  }
document.write("<a class='btn navbar-btn btn-social-icon navbar-btn' href='mailto:"+link+"'><i class='fas fa-envelope' style='color:#cc724f'></i></a>")
}