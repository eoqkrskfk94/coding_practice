import kotlin.math.max

fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()
    var totalStairCount = br.readLine().toInt()
    var stairs = List(totalStairCount) { 0 }.toMutableList()
    var stairsDp = List(totalStairCount) { 0 }.toMutableList()

    for(i in 0 until totalStairCount) {
        stairs[i] = br.readLine().toInt()
    }

    for(i in 0 until totalStairCount) {
        when(i) {
            0 -> stairsDp[0] = stairs[0]
            1 -> stairsDp[1] = stairs[1] + stairs[0]
            2 -> stairsDp[2] = max(stairs[2] + stairs[1], stairs[2] + stairs[0])
            else -> {
                stairsDp[i] = max(stairs[i] + stairs[i-1] + stairsDp[i-3], stairs[i] + stairsDp[i-2])
            }
        }
    }

    println(stairsDp[totalStairCount-1])
}




