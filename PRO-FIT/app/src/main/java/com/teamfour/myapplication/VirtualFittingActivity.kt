package com.teamfour.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.LinearLayout
import androidx.recyclerview.widget.LinearLayoutManager
import com.teamfour.myapplication.databinding.ActivityVirtualFittingBinding

class VirtualFittingActivity : BaseActivity() {

    val binding by lazy {ActivityVirtualFittingBinding.inflate(layoutInflater)}
    lateinit var rcyAdapter:VirtualFittingVideoAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        setTitle("MY VIDEO")

        init()
    }

    private fun init(){
        binding.virtualRcyView.layoutManager = LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false)
        rcyAdapter = VirtualFittingVideoAdapter()
        //클릭 했을때 이벤트

        binding.virtualRcyView.adapter = rcyAdapter

        binding.addVideoBtn.setOnClickListener {
            //새 동영상 촬영
        }

    }

}