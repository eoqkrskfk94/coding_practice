fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()

    var (coin, price) = br.readLine()!!.split(" ").map {it.toInt()}
    var coinList = Array(coin, {0})
    var totalCoinCount = 0

    for (i in coinList.indices) {
        coinList[i] = br.readLine().toInt()
    }

    for(i in coinList.indices.reversed()) {

        if(coinList[i] <= price) {
            val temp = price % coinList[i]
            totalCoinCount += price / coinList[i]
            price = temp

            if(price == 0) break
        }
    }

    println(totalCoinCount)


}