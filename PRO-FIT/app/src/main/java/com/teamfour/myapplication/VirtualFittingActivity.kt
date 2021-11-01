package com.teamfour.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.teamfour.myapplication.databinding.ActivityVirtualFittingBinding

class VirtualFittingActivity : BaseActivity() {

    val binding by lazy {ActivityVirtualFittingBinding.inflate(layoutInflater)}

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)
    }
}