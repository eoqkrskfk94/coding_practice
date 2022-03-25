import kotlin.math.max

fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()
    val wordCount = br.readLine().toInt()
    var list = mutableListOf<List<Int>>()

    repeat(wordCount) {
        list.add(br.readLine().split(" ").map { it.toInt() })
    }

    val result = list.sortedWith { a, b ->
        if (a[0] > b[0]) {
            1
        } else if (a[0] == b[0]) {
            if (a[1] > b[1]) 1
            else -1
        } else {
            -1
        }
    }

    result.forEach {
        println(it.joinToString(" "))
    }


}






