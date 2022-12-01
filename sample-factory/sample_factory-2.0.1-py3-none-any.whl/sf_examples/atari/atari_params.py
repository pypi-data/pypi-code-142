def atari_override_defaults(_env, parser):
    """RL params specific to Atari envs."""
    parser.set_defaults(
        # let's set this to True by default so it's consistent with how we report results for other envs
        # (i.e. VizDoom or DMLab). When running evaluations for reports or to compare with other frameworks we can
        # set this to false in command line
        summaries_use_frameskip=True,
        use_record_episode_statistics=True,
        encoder_conv_architecture="convnet_atari",
        obs_scale=255.0,
        gamma=0.99,
        env_frameskip=4,
        env_framestack=4,
        exploration_loss_coeff=0.01,
        num_workers=8,
        num_envs_per_worker=1,
        worker_num_splits=1,
        train_for_env_steps=10000000,
        nonlinearity="relu",
        kl_loss_coeff=0.0,
        use_rnn=False,
        adaptive_stddev=False,
        reward_scale=1.0,
        with_vtrace=False,
        recurrence=1,
        batch_size=256,
        rollout=128,
        max_grad_norm=0.5,
        num_epochs=4,
        num_batches_per_epoch=4,
        ppo_clip_ratio=0.1,
        value_loss_coeff=0.5,
        exploration_loss="entropy",
        learning_rate=0.00025,
        lr_schedule="linear_decay",
        shuffle_minibatches=False,
        gae_lambda=0.95,
        batched_sampling=False,
        normalize_input=True,
        normalize_returns=True,
        serial_mode=False,
        async_rl=False,
        experiment_summaries_interval=3,
        adam_eps=1e-5,  # choosing the same value as CleanRL used
    )
