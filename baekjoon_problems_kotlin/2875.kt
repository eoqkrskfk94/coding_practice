fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()

    var (n, m, k) = br.readLine().split(" ").map { it.toInt() }


    for(i in n downTo 0) {
        var girlsLeft = n
        var boysLeft = m
        if(i % 2 == 0) {
            girlsLeft -= i
            boysLeft -= i/2

            if(boysLeft < 0) {
                continue
            } else {
                if(girlsLeft + boysLeft >= k) {
                    println(i/2)
                    break
                }
            }
        }
    }

}



