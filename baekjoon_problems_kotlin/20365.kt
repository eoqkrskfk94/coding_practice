import kotlin.math.*

fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()
    val count = br.readLine().toInt()
    var str = br.readLine()

    var prevColor = 'Z'
    var blues = 0
    var reds = 0

    str.forEach {
        if(it != prevColor) {
            prevColor = it
            when(it) {
                'B' -> blues++
                'R' -> reds++
            }
        }
    }

    if(blues == reds) {
        println(blues+1)
    } else if(blues > reds) {
        println(reds+1)
    } else {
        println(blues+1)
    }


}










