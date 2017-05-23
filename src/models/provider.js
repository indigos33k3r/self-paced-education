import mongoose from 'mongoose';

const Schema = mongoose.Schema;

export const Provider = new Schema({
    name: { type: String, required: true },
    url: { type: String, required: true }
});
