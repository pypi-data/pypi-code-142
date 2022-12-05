"""
source_batch = <tf.Tensor 'source_batch:0' shape=(None,) dtype=string>
sim = <tf.Tensor 'while/StatefulPartitionedCall:0' shape=<unknown> dtype=float32>
source_batch[i] = <tf.Tensor 'while/strided_slice_3:0' shape=() dtype=string>

"""

import tensorflow as tf
import tensorflow_text as tf_text


distance_matrix = tf.Variable(tf.zeros([1000, 1000], tf.int32))

@tf.function(input_signature=[
    tf.TensorSpec([None], tf.int32),
    tf.TensorSpec([None], tf.int32),
    tf.TensorSpec(None, tf.int32),
    tf.TensorSpec(None, tf.int32),
    tf.TensorSpec(None, tf.int32),
])
def tf_codepoint_lev(
        source,
        target,
        delete=tf.constant(1),
        insert=tf.constant(1),
        substitute=tf.constant(2),
    ):
    """
    source, target: an array of codepoints
    """
    m = tf.shape(source)[0]
    n = tf.shape(target)[0]
    distance_matrix[:m+1, :n+1].assign(tf.zeros([m+1, n+1], tf.int32))

    start = delete
    delta = delete
    limit = (m+1) * delete
    distance_matrix[1:m+1, 0].assign(tf.range(start, limit, delta))

    start = insert
    step = insert
    limit = (n+1) * insert
    distance_matrix[0, 1:n+1].assign(tf.range(start, limit, delta))

    for i in tf.range(1, m+1):
        for j in tf.range(1, n+1):
            cond = source[i-1] == target[j-1]
            candidates = [
                distance_matrix[i-1, j-1] + tf.cond(
                    cond,
                    lambda: tf.constant(0),
                    lambda: substitute,
                ),
                distance_matrix[i-1, j] + delete,
                distance_matrix[i, j-1] + insert,
            ]
            #candidates = tf.constant([
            #    distance_matrix[i-1, j-1] + tf.cond(
            #        cond,
            #        lambda: tf.constant(0),
            #        lambda: substitute,
            #    ),
            #    distance_matrix[i-1, j] + delete,
            #    distance_matrix[i, j-1] + insert,
            #])
            distance_matrix[i,j].assign(tf.reduce_min(candidates))

    #return distance_matrix.value()[m, n]
    return distance_matrix[m, n]


@tf.function(input_signature=[
    tf.TensorSpec([], tf.string),
    tf.TensorSpec([], tf.string),
    tf.TensorSpec(None, tf.int32),
    tf.TensorSpec(None, tf.int32),
    tf.TensorSpec(None, tf.int32),
])
def tf_byte_lev(
        source,
        target,
        delete=tf.constant(1),
        insert=tf.constant(1),
        substitute=tf.constant(2),
    ):
    source = tf_text.normalize_utf8(source, "NFKD")
    target = tf_text.normalize_utf8(target, "NFKD")
    source = tf.strings.unicode_decode(source, "UTF-8")
    target = tf.strings.unicode_decode(target, "UTF-8")
    return tf_codepoint_lev(
                source,
                target,
                delete,
                insert,
                substitute,
            )


@tf.function(
    input_signature=[
        tf.TensorSpec([None], tf.string),
        tf.TensorSpec([None], tf.string),
        tf.TensorSpec(None, tf.int32),
        tf.TensorSpec(None, tf.int32),
        tf.TensorSpec(None, tf.int32),
    ],
)
def tf_batch_lev(
        source_batch,
        target_batch,
        delete=tf.constant(1),
        insert=tf.constant(1),
        substitute=tf.constant(2),
    ):
    batch_size = tf.shape(source_batch)[0]
    somme = tf.constant(0.)
    for i in tf.range(batch_size):
        dist = tf_byte_lev(
            source_batch[i],
            target_batch[i],
            delete,
            insert,
            substitute,
        )
        somme += tf.cast(dist, tf.float32)

    avg = somme / tf.cast(batch_size, tf.float32)
    return avg


@tf.function(
    input_signature=[
        tf.TensorSpec([], tf.string),
        tf.TensorSpec([], tf.string),
        tf.TensorSpec(None, tf.int32),
        tf.TensorSpec(None, tf.int32),
        tf.TensorSpec(None, tf.int32),
        tf.TensorSpec(None, tf.bool),
        tf.TensorSpec(None, tf.float32),
    ],
    autograph=True,
)
def tf_byte_sim(
        source,
        target,
        delete=tf.constant(1),
        insert=tf.constant(1),
        substitute=tf.constant(2),
        proportional=tf.constant(True),
        alpha=tf.constant(1/3),
    ):
    source = tf_text.normalize_utf8(source, "NFKD")
    target = tf_text.normalize_utf8(target, "NFKD")
    source = tf.strings.unicode_decode(source, "UTF-8")
    target = tf.strings.unicode_decode(target, "UTF-8")

    dist = tf_codepoint_lev(source, target, delete,
                            insert, substitute)
    dist = tf.cast(dist, tf.float32)
    len_target = tf.shape(target)[0]
    len_target = tf.cast(len_target, tf.float32)
    substitute_float32 = tf.cast(substitute, tf.float32)
    if proportional:
        #proportion = dist / (
        #    substitute_float32 * tf.maximum(
        #        tf.constant(1.),
        #        len_target
        #))
        proportion = tf.math.divide(
            dist,
            substitute_float32 * tf.maximum(
                tf.constant(1.),
                len_target
            )
        )
        #similarity = (
        #    tf.constant(1.)
        #    - tf.minimum(
        #          tf.constant(1.),
        #          proportion
        #      )
        #)
        similarity = tf.math.subtract(
            tf.constant(1.),
            tf.minimum(
                tf.constant(1.),
                proportion
            )
        )
    else:
        if dist > len_target*substitute_float32:
            similarity = tf.constant(0.)
        else:
            similarity = (
                tf.constant(1.)
                / (alpha*dist + tf.constant(1.))
            )
    similarity = tf.ensure_shape(similarity, [])
    #print(f"{similarity = }")
    return similarity


@tf.function(
    input_signature=[
        tf.TensorSpec([None], tf.string),
        tf.TensorSpec([None], tf.string),
        tf.TensorSpec(None, tf.int32),
        tf.TensorSpec(None, tf.int32),
        tf.TensorSpec(None, tf.int32),
        tf.TensorSpec(None, tf.bool),
        tf.TensorSpec(None, tf.float32),
    ],
    #autograph=True,
)
def tf_batch_sim(
        source_batch,
        target_batch,
        delete=tf.constant(1),
        insert=tf.constant(1),
        substitute=tf.constant(2),
        proportional=tf.constant(True),
        alpha=tf.constant(1/3),
    ):
    batch_size = tf.shape(source_batch)[0]
    #batch_size = source_batch.shape[0]
    #print(f"\n{source_batch = }")
    somme = tf.constant(0.)
    for i in tf.range(batch_size):
        #tf.autograph.experimental.set_loop_options(
        #    shape_invariants=[
        #        (somme, tf.TensorShape(()))
        #    ]
        #)
        #tf.autograph.experimental.set_loop_options(maximum_iterations=128)

        #somme = somme + tf_byte_sim(
        #        source_batch[i],
        #        target_batch[i],
        #        delete,
        #        insert,
        #        substitute,
        #        proportional,
        #        alpha,
        #    )

        sim = tf_byte_sim(
            source_batch[i],
            target_batch[i],
            delete,
            insert,
            substitute,
            proportional,
            alpha,
        )
        # TODO: tf.add() and +=, diff?
        somme = tf.add(somme, sim)
        #somme += sim

    avg = somme / tf.cast(batch_size, tf.float32)
    return avg


