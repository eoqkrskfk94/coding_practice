import kotlin.math.*

fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()

    var str = br.readLine()
    var str2 = str.reversed()

    var duplicateCount = 0

    for(i in str.length - 1 downTo  0) {


        if(str.substring(i,str.length) == str2.substring(0,str2.length - i)) {
            duplicateCount = max(duplicateCount, str.length - i)
        }
    }



    println(str.length * 2 - duplicateCount)
}










