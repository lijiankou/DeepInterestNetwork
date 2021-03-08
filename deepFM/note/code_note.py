def __init__(self, user_count, item_count, cate_count, cate_list):
  #u  user_id
  #i 正样本 item_id
  #j 负样本 item_id
  #hist_i history item list
  #y label (0,1)
  #cate_list item到cate的映射关系, tf 
  self.u = tf.placeholder(tf.int32, [None,]) # [B]
  self.i = tf.placeholder(tf.int32, [None,]) # [B]
  self.j = tf.placeholder(tf.int32, [None,]) # [B]
  self.y = tf.placeholder(tf.float32, [None,]) # [B]
  self.hist_i = tf.placeholder(tf.int32, [None, None]) # [B, T]
  self.sl = tf.placeholder(tf.int32, [None,]) # [B]
  self.lr = tf.placeholder(tf.float64, [])

  hidden_units = 128


