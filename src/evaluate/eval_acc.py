# -*- coding: utf-8 -*-
from mindspore.train.callback import Callback

class StepLossAccInfo(Callback):
    def __init__(self, model, eval_dataset, steps_loss, steps_eval):
        self.model = model
        self.eval_dataset = eval_dataset
        self.steps_loss = steps_loss
        self.steps_eval = steps_eval

    def step_end(self, run_context):
        cb_params = run_context.original_args()
        cur_epoch = cb_params.cur_epoch_num
        cur_step = (cur_epoch - 1) * 2975 + cb_params.cur_step_num
        self.steps_loss["loss_value"].append(str(cb_params.net_outputs))
        self.steps_loss['step'].append(str(cur_step))
        if cur_step % 2975 == 0 and cur_epoch % 20 == 0:
            acc = self.model.eval(self.eval_dataset, dataset_sink_mode=False)
            self.steps_eval['step'].append(cur_step)
            self.steps_eval['acc'].append(acc["accuracy"])
            print("epoch:{}, step:{}, acc: {}".format(cur_epoch, cur_step, acc['accuracy']))

