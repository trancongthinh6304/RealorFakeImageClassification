import tensorflow as tf

def train_model(model, lr, model_name,  nb_of_epoch, step_per_epoch, val_step, min_lr, train_generator, val_generator):
    ## Freeze all the layers before the `fine_tune_at` layer
    #for layer in base_model.layers[:fine_tune_at]:
    #    layer.trainable =  False
    print('--------------Deploying the Model...--------------')
    model.compile(loss = 'binary_crossentropy', 
                  optimizer = tf.keras.optimizers.Adam(learning_rate=lr),
                  metrics = 'accuracy')
    monitor = tf.keras.callbacks.EarlyStopping(monitor = 'val_loss', 
                                               min_delta = 1e-4, 
                                               patience = 10, 
                                               verbose = 1, 
                                               mode = 'min',
                                               restore_best_weights = True)
    lr_scheduler = tf.keras.callbacks.ReduceLROnPlateau(monitor = "val_loss",
                                                        factor = 0.5,
                                                        patience = 3,
                                                        verbose = 1,
                                                        mode = 'min',
                                                        min_delta = 1e-4,
                                                        cooldown = 0,
                                                        min_lr = min_lr)

    filepath = model_name + "-{epoch:02d}-{val_loss:.4f}.hdf5"
    checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath, 
                                                    monitor = 'val_loss', 
                                                    verbose = 1, 
                                                    save_best_only = False, 
                                                    save_weights_only = True, 
                                                    mode = 'min',
                                                    save_freq = 'epoch')
    print('--------------Deployed Successfully--------------')
    print('--------------Training Begins--------------')
    history = model.fit(train_generator, 
                        epochs = nb_of_epoch, 
                        steps_per_epoch = step_per_epoch, 
                        validation_data = val_generator, 
                        verbose = 1, 
                        validation_steps = val_step,
                        callbacks = [monitor,lr_scheduler,checkpoint])
    return history