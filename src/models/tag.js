import mongoose from 'mongoose';

const Schema = mongoose.Schema;

export const Tag = new Schema({
    name: { type: String, required: true },
});
