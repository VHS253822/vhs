var names = ["Yaakov", "John", "Jen", "Jason", "Paul", "Frank", "Larry", "Paula", "Laura", "Jim"];

for (i=0; i<names.length; i++)
{
 if ((names[i][0].startsWith("J",0))==true)
 {
     goodbye.speak(names[i]);
  } 
  else
  {
    hello.speak(names[i]);
  }
}