import kotlin.math.max

fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()

    val numberCount = br.readLine().toInt()
    val numberList = br.readLine().split(" ").map { it.toInt() }
    var dp = MutableList(numberCount) { 0 }

    var maxNumber = Integer.MIN_VALUE

    for (i in 0 until numberCount) {
        when (i) {
            0 -> {
                dp[0] = numberList[0]
                maxNumber = max(maxNumber, dp[0])
            }
            else -> {
                dp[i] = max(numberList[i] + dp[i - 1], numberList[i])
                maxNumber = max(maxNumber, dp[i])
            }
        }
    }

    println(maxNumber)

}




