__author__ = 'XJH'
import tensorflow as tf

# 创建常量op 产生一个1×2矩阵 这个op被作为一个节点
# 加到默认图中

# 构造器的返回值代表该常量 op 的返回值
# matrix1 = tf.constant([[3., 3.]])
# print(matrix1)

# 创建常量 op， 产生一个2×1矩阵
# matrix2 = tf.constant([[2.], [2.]])

# 创建矩阵乘法 matmul op
# 返回值为矩阵乘法的结果
# product = tf.matmul(matrix1, matrix2)

# 启动默认图
# sess = tf.Session()

# 调用 sess 的 'run()' 方法来执行矩阵乘法 op, 传入 'product' 作为该方法的参数.
# 上面提到, 'product' 代表了矩阵乘法 op 的输出, 传入它是向方法表明, 我们希望取回
# 矩阵乘法 op 的输出.
#
# 整个执行过程是自动化的, 会话负责传递 op 所需的全部输入. op 通常是并发执行的.
#
# 函数调用 'run(product)' 触发了图中三个 op (两个常量 op 和一个矩阵乘法 op) 的执行.
#
# 返回值 'result' 是一个 numpy `ndarray` 对象.
# print(sess.run(matrix1))
# print(sess.run(matrix2))
# result = sess.run(product)
# print(result)

#任务完成 关闭会话
# sess.close()

# 使用with代码块
# with tf.Session() as sess:
# 	result = sess.run([product])
# 	print(result)

# 创建一个变量 初始化为标量0
# state = tf.Variable(0, name="counter")

# 创建一个 op，其作用是使state增加 1
# one = tf.constant(1)
# new_value = tf.add(state, one)
# update = tf.assign(state, new_value)

# 启动图后, 变量必须先经过`初始化` (init) op 初始化,
# 首先必须增加一个`初始化` op 到图中.
# init_op = tf.initialize_all_variables()

# 启动图 运行op
# with tf.Session() as sess:
	# 运行 'init' op
	# sess.run(init_op)
	# 打印 'state' 的初始值
	# print(sess.run(state))
	# 运行 op，更新 'state'，并打印 'state'
	# for _ in range(3):
	# 	sess.run(update)
	# 	print(sess.run(state))

# input1 = tf.constant(3.0)
# input2 = tf.constant(2.0)
# input3 = tf.constant(5.0)
#
# intermed = tf.add(input2, input3)
# mul = tf.multiply(input1, intermed)
#
# with tf.Session() as sess:
# 	result = sess.run([mul, intermed])
# 	print(result)

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

with tf.Session() as sess:
	print(sess.run([output], feed_dict={input1:[7.0], input2:[2.]}))
