import kotlin.math.max

fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()
    val wordCount = br.readLine().toInt()
    var list = mutableListOf<String>()

    repeat(wordCount) {
        list.add(br.readLine().toString())
    }

    list = list.toSet().toMutableList()

    val result = list.sortedWith { a, b ->
        if (a.length > b.length) 1
        else if (a.length == b.length) {
            if (a > b) 1
            else -1
        } else {
            -1
        }
    }

    result.forEach {
        println(it)
    }

}






