import kotlin.math.max

fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()
    var totalWineCount = br.readLine().toInt()
    var wineAmount = List(totalWineCount) { 0 }.toMutableList()
    var wineDp = List(totalWineCount) { 0 }.toMutableList()
    var maxAmount = 0

    for(i in 0 until totalWineCount) {
        wineAmount[i] = br.readLine().toInt()
    }

    for(i in 0 until totalWineCount) {
        when(i) {
            0 -> {
                wineDp[0] = wineAmount[0]
                maxAmount = max(maxAmount, wineDp[0])
            }
            1 -> {
                wineDp[1] = wineAmount[1] + wineAmount[0]
                maxAmount = max(maxAmount, wineDp[1])
            }
            2 -> {
                wineDp[2] = max(max(wineAmount[2] + wineAmount[1], wineAmount[2] + wineAmount[0]), wineAmount[0] + wineAmount[1])
                maxAmount = max(maxAmount, wineDp[2])
            }
            else -> {
                val try1 = wineDp[i-1]
                val try2 = wineAmount[i] + wineDp[i-2]
                val try3 = wineAmount[i] + wineAmount[i-1] + wineDp[i-3]
                wineDp[i] = max(max(try1 , try2), try3)
                maxAmount = max(maxAmount, wineDp[i])
            }
        }
    }

    println(maxAmount)
}




