/*
	URL = https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/
*/

fun main(args: Array<String>) {
    println(canConstruct("bg","efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
    
}
 fun canConstruct(ransomNote: String, magazine: String):Boolean{
     
     
     return if(ransomNote.isEmpty())     {
         true
     }
     else if(ransomNote.isNotEmpty() && magazine.isEmpty()) {
         false
     }
     else {
         
        for(i in 0 until ransomNote.length)
        {
            val char = ransomNote[i]
            println("Char : $char")
            if(magazine.contains(char)) {
                val mazagineCharCount = magazine.filter  { it==char }.count()
                val ransomNoteCharCount = ransomNote.filter  {  it==char}.count()
                println("Magazine Char Count : $mazagineCharCount")
                println("Ransom Char Count : $ransomNoteCharCount")
                if(mazagineCharCount<ransomNoteCharCount){
                    return false
                }                
            }
            else {
                return false
            }

        }
        true
    }
        
    }
