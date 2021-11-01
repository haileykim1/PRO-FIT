package com.teamfour.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.teamfour.myapplication.databinding.ActivityProfileBinding

class ProfileActivity : AppCompatActivity() {

    val binding by lazy {ActivityProfileBinding.inflate(layoutInflater)}

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)
    }
}