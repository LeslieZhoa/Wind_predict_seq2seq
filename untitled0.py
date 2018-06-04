import numpy as np
import tensorflow as tf
import h5py
import random
slim=tf.contrib.slim
# Optmizer: 
learning_rate = 0.007  # Small lr helps not to diverge during training. 
nb_iters = 10000  # How many times we perform a training step (therefore how many times we show a batch). 
lr_decay = 0.92  # default: 0.9 . Simulated annealing.
momentum = 0.5  # default: 0.0 . Momentum technique in weights update
lambda_l2_reg = 0.003  # L2 regularization of weights - avoids overfitting
x=tf.placeholder(tf.float32,[None,2])
y=tf.placeholder(tf.float32,[None,1])
with slim.arg_scope([slim.layers.fully_connected],weights_initializer=slim.xavier_initializer(),activation_fn=tf.nn.relu):
    net=slim.fully_connected(x,4,scope='fc1')
#     net=slim.fully_connected(net,8,scope='fc2')
    net=slim.fully_connected(net,4,scope='fc3')
    output=slim.fully_connected(net,1,activation_fn=None,scope='fc4')
# Training loss and optimizer

with tf.variable_scope('Loss'):
    # L2 loss
   
    output_loss = tf.reduce_mean(tf.nn.l2_loss(output - y))
        
    # L2 regularization (to avoid overfitting and to have a  better generalization capacity)
    reg_loss = 0
    for tf_var in tf.trainable_variables():
        if not ("Bias" in tf_var.name or "Output_" in tf_var.name):
            reg_loss += tf.reduce_mean(tf.nn.l2_loss(tf_var))
            
    loss = output_loss + lambda_l2_reg * reg_loss
    tf.summary.scalar('loss',loss)

with tf.variable_scope('acc'):
    acc = tf.reduce_mean(tf.nn.l2_loss(y-output))/tf.reduce_mean(tf.nn.l2_loss(y-0))
    
    acc=1-acc
    tf.summary.scalar('acc',acc)

with tf.variable_scope('Optimizer'):
    optimizer = tf.train.RMSPropOptimizer(learning_rate, decay=lr_decay, momentum=momentum)
    train_op = optimizer.minimize(loss)
    merged_summary = tf.summary.merge_all()
    
min_loss=10000
sess=tf.Session()
saver=tf.train.Saver()
model_file=tf.train.latest_checkpoint('D:/model/fitted/')
saver.restore(sess,model_file)
out=sess.run(output,feed_dict={x:xt})



sess.close()