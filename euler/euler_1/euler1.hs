-- Solution 1
divN :: Int -> Int -> Bool
divN x y = (x `mod` y) == 0

factors :: Int -> [Int]
factors n = [x | x <- [1..n], x `divN` 3 || x `divN` 5]

-- Solution 2
divisibleBy :: Integral a => a -> a -> Bool
divisibleBy x y = (x `mod` y) == 0

factors2 :: Int -> [Int]
factors2 n = [x | x <- [1..n], x `divisibleBy` 3 || x `divisibleBy` 5]

-- Solution 3
divisibleB :: Int -> Int -> Bool
divisibleB x y = (x `mod` y) == 0

factors3 :: Int -> [Int]
factors3 n = [x | x <- [1..n], x `divisibleB` 3 || x `divisibleB` 5]
