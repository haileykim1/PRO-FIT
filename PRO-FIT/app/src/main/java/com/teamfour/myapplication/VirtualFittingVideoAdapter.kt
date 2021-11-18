package com.teamfour.myapplication

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class VirtualFittingVideoAdapter: RecyclerView.Adapter<VirtualFittingVideoAdapter.VirtualFittingVideoViewHolder>() {

    interface OnItemClickListener{
        fun onItemClick(holder: VirtualFittingVideoViewHolder, view: View, data: Int, position: Int)
    }

    var itemClickListener: OnItemClickListener? = null

    inner class VirtualFittingVideoViewHolder(itemView: View): RecyclerView.ViewHolder(itemView){
        var textTitleView: TextView = itemView.findViewById(R.id.VirtualRcyImage)
        var imageView: ImageView = itemView.findViewById(R.id.VirtualRcyTitle)
        init{
            itemView.setOnClickListener{
                val size = itemCount - 1
                itemClickListener?.OnItemClick(this, it, 0, size - adapterPosition)
            }
        }

    }

    override fun onCreateViewHolder(
        parent: ViewGroup,
        viewType: Int
    ): VirtualFittingVideoViewHolder {
        val v: View = LayoutInflater.from(parent.context).inflate(R.layout.virtualfitting_videoitem, parent, false)
        return VirtualFittingVideoViewHolder(v)
    }

    override fun onBindViewHolder(holder: VirtualFittingVideoViewHolder, position: Int) {
        val size = itemCount - 1
        //holder.textTitleView.text =
        //holder.imageView
    }

    override fun getItemCount(): Int {
        return itemCount
    }

}