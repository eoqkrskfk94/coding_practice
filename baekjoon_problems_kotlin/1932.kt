import kotlin.math.max

fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()

    val height = br.readLine().toInt()
    var stairs = mutableListOf<List<Int>>()
    var stairsDp = mutableListOf<List<Int>>()

    for(i in 0 until height) {
        stairs.add(br.readLine().split(" ").map { it.toInt() })
    }

    stairs = stairs.reversed().toMutableList()
    stairsDp.add(stairs[0])

    for(i in 1 until height) {
        var temp = mutableListOf<Int>()
        for(j in 0 until stairs[i].size) {
            val bestChoice = max(stairs[i][j] + stairsDp[i-1][j], stairs[i][j] + stairsDp[i-1][j+1])
            temp.add(bestChoice)
        }
        stairsDp.add(temp)
    }

    println(stairsDp[height-1][0])



}




