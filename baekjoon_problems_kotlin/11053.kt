import kotlin.math.max

fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()

    val totalNumberCount = br.readLine().toInt()

    val numberList = br.readLine().split(" ").map { it.toInt() }
    val dp = MutableList(totalNumberCount) { 1 }
    var maxSeriesCount = 1

    for(i in numberList.indices) {
        for (j in 0 until i) {
            if(numberList[i] > numberList[j]) {
                dp[i] = max(dp[i], dp[j] + 1)
                maxSeriesCount = max(maxSeriesCount, dp[i])
            }
        }
    }

    println(maxSeriesCount)
}




